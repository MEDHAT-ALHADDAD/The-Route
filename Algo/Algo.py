from APIserver import calccost
debug = True
THREADIT = True
def debugPrint(thing):
    if debug:
        print(thing)



import time
import threading
from APIserver import costThread
infinity = 90000000
# arr = [\
#     [0,3,4,infinity,90],\
#     [3,0,5,2,8],\
#     [4,5,0,55,9],\
#     [infinity,2,55,0,5],
#     [1,2,3,4,0]]

counter = 0
# def calccost(src, dst, date):
    # return arr[src][dst]
startCity = "HND"

#The only job for this thread is to call the recursive function in a new thread of execution
class TSPThread(threading.Thread):
    def setinput(self, node, leftover:set):
        self.node = node
        self.leftover = leftover
    def run(self):
        self.cost, self.path = tsp(self.node, self.leftover)
    def getanswer(self):
        return self.cost, self.path



def tsp(node, leftover:set) -> (int, list) : #returns the min cost from node and the last set of nodes we need to go after node
    global counter  # to count nodes in binary tree of this recursive function
                    # due to recursions this count is probably wrong
    counter += 1
    if len(leftover) == 0:
        return (calccost(node,startCity), [node, startCity]) # base case where last city in order returns to hometown
    mn = infinity # the minimum cost
    mnpath = [] # the order of the cities on the best path
    threads = []
    tspthreads = []
    for i,city in enumerate(leftover):
        thread = costThread() # a thread to do http requets
        thread.setinput(node, city)
        tspthread = TSPThread() # a thread to handle recursions
        tspthread.setinput(city, leftover - set([city]))
        if THREADIT:
            thread.start()
            tspthread.start()
        else:# thread.run() works sequentially
            thread.run()
            tspthread.run()
        threads.append(thread)
        tspthreads.append(tspthread)
    if THREADIT:
        for t in threads:
            t.join()
        for t in tspthreads:
            t.join()
    for i,city in enumerate(leftover):
        # tmpcost, path = tsp(city, leftover - set([city])) #tmpcost is the cost from city to the rest of the set
        # debugPrint("path: ", path)
        tmpcost, path = tspthreads[i].getanswer()   # tmp ccost is the cost of the chain from recursion tree
                                                    #   from city to home town passing through leftover cities
        current = tmpcost + threads[i].totalcost #current is cost from node to city + tmpcost
        if(mn > current):
            mn = current
            mnpath = path
    return (mn, [node] + mnpath)

start = time.time()
debugPrint(tsp(startCity, set(["ATL", "ORD", "DXB", "LAX", "LHR"])))
end = time.time()

# ["ATL", "PEK", "DXB", "LAX"]
print("time taken is {} seconds".format(end - start))
debugPrint(counter)