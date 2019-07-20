from APIserver import calccost
debug = False
THREADIT = False
def debugPrint(thing):
    if debug:
        print(thing)



import time
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
def tsp(node:int, leftover:set) -> (int, list) : #returns the min cost from node and the last set of nodes we need to go after node
    global counter
    counter += 1
    # debugPrint("loading")
    if len(leftover) == 0:
        return (calccost(node,startCity), [node, startCity]) #
    mn = infinity
    mnpath = []
    threads = []
    for i,city in enumerate(leftover):
        thread = costThread()
        thread.setinput(node, city)
        if THREADIT:
            thread.start()
        else:
            thread.run()
        threads.append(thread)
    if THREADIT:
        for t in threads:
            t.join()
    for i,city in enumerate(leftover):
        tmpcost, path = tsp(city, leftover - set([city])) #tmpcost is the cost from city to the rest of the set
        # debugPrint("path: ", path)
        current = tmpcost + threads[i].totalcost #current is cost from node to city + tmpcost
        if(mn > current):
            mn = current
            mnpath = path
    return (mn, [node] + mnpath)

start = time.time()
debugPrint(tsp(startCity, set(["ATL", "JFK", "DXB"])))
end = time.time()

# ["ATL", "PEK", "DXB", "LAX"]
print("time taken is {} seconds".format(end - start))
debugPrint(counter)