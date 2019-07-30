import time
import datetime
import threading
from . import node
from . import flight
# from APIserver import costThread
from . import APIserver
from . import CONST


# IMPORTANT
# This method is the only way to calculate the cost from this module
# ALL other methods should not be called
def maincalccost(start:node.node, mid, end:node.node, startdate:datetime.datetime) -> (int, list) :
    global startCity, endCity
    startCity = start
    endCity = end
    return tsp(startCity,set(mid),startdate)





counter = 0

#The only job for this thread is to call the recursive function in a new thread of execution
class TSPThread(threading.Thread):
    def setinput(self, node, leftover:set, startdate: datetime.datetime):
        self.node = node
        self.leftover = leftover
        self.startdate = startdate
    def run(self):
        self.cost, self.path = tsp(self.node, self.leftover, self.startdate)
    def getanswer(self):
        return self.cost, self.path



def tsp(node:node.node, leftover:set, startdate:datetime.datetime) -> (int, list) : #returns the min cost from node and the last set of nodes we need to go after node
    global counter  # to count nodes in binary tree of this recursive function
                    # due to recursions this count is probably wrong
    counter += 1
    if len(leftover) == 0:
        tflight = APIserver.calccost(node,endCity, startdate+node.duration)
        return (tflight.price, [tflight]) # base case where last city in order returns to hometown
    mn = CONST.infinity # the minimum cost
    mnpath = [] # the order of the cities on the best path
    mnflight = 0 # the minimum cost flight to be chosen
    threads = []
    tspthreads = []
    nextstartdate = startdate + node.duration
    if not CONST.TURBOMODE:
        for i,city in enumerate(leftover):
            thread = APIserver.costThread() # a thread to do http requets
            thread.setinput(node, city, nextstartdate)
            if CONST.THREADIT:
                thread.start()
            else:# thread.run() works sequentially
                thread.run()
            threads.append(thread)
        if CONST.THREADIT:
            for t in threads:
                t.join()
        for i,city in enumerate(leftover):
            tspthread = TSPThread() # a thread to handle recursions
            tspthread.setinput(city, leftover - set([city]), nextstartdate)
            if CONST.THREADIT:
                tspthread.start()
            else:# thread.run() works sequentially
                tspthread.run()
            tspthreads.append(tspthread)
        if CONST.THREADIT:
            for t in tspthreads:
                t.join()
    else:
            for i,city in enumerate(leftover):
                thread = APIserver.costThread() # a thread to do http requets
                thread.setinput(node, city, nextstartdate)
                tspthread = TSPThread() # a thread to handle recursions
                tspthread.setinput(city, leftover - set([city]), nextstartdate)
                if CONST.THREADIT:
                    tspthread.start()
                    thread.start()
                else:# thread.run() works sequentially
                    tspthread.run()
                    thread.run()
                tspthreads.append(tspthread)
                threads.append(thread)
            if CONST.THREADIT:
                for t in tspthreads:
                    t.join()
                for t in threads:
                    t.join()
    for i,city in enumerate(leftover):
        # tmpcost, path = tsp(city, leftover - set([city])) #tmpcost is the cost from city to the rest of the set
        # CONST.debugPrint("path: ", path)
        tmpcost, path = tspthreads[i].getanswer()   # tmp ccost is the cost of the chain from recursion tree
                                                    #   from city to home town passing through leftover cities
        tflight = threads[i].getresults()
        current = tmpcost + tflight.price #current is cost from node to city + tmpcost
        if(mn > current):
            mn = current
            mnpath = path
            mnflight = tflight
    return (mn, [mnflight] + mnpath)

startCity = node.node(datetime.timedelta(0),"","HND")
endCity = startCity


def test():
    start = time.time()
    initial = datetime.datetime(2019,7,20) + datetime.timedelta(days=90)
    nodes = set()
    nodes.add(node.node(datetime.timedelta(days=3),"", "ATL"))
    nodes.add(node.node(datetime.timedelta(days=4),"", "ORD"))
    nodes.add(node.node(datetime.timedelta(days=9),"", "DXB"))
    nodes.add(node.node(datetime.timedelta(days=2),"", "LAX"))
    nodes.add(node.node(datetime.timedelta(days=4),"", "LHR"))
    nodes.add(node.node(datetime.timedelta(days=5),"", "PEK"))
    CONST.debugPrint("testing {} cities plus the hometown".format(len(nodes)))
    cost, path = tsp(startCity, nodes,initial)
    CONST.debugPrint("total cost: {}".format(cost))
    for p in path:
        CONST.debugPrint(p)
    end = time.time()
    print("time taken to run algorithm is {} seconds".format(end - start))
    CONST.debugPrint("number of function calls: {}".format(counter))