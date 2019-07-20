import random

infinity = 90000000
arr = [\
    [0,3,4,infinity,90],\
    [3,0,5,2,8],\
    [4,5,0,55,9],\
    [infinity,2,55,0,5],
    [1,2,3,4,0]]

counter = 0
def calccost(src, dst, date):
    return arr[src][dst]

def tsp(node:int, leftover:set) -> (int, list) : #returns the min cost from node and the last set of nodes we need to go after node
    if len(leftover) == 0:
        return (calccost(node,0,0), [node, 0]) #
    mn = infinity
    mnpath = []
    global counter
    counter += 1
    for city in leftover:
        tmpcost, path = tsp(city, leftover - set([city])) #tmpcost is the cost from city to the rest of the set
        # print("path: ", path)
        current = tmpcost + calccost(node,city,0) #current is cost from node to city + tmpcost
        if(mn > current):
            mn = current
            mnpath = path
    return (mn, [node] + mnpath)

print(tsp(0, set([1,2,3,4])))
print(counter)