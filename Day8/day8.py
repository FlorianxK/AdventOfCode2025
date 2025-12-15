import heapq
from typing import *

def dayEight():
    arr = []
    pairs = 1000
    #read
    with open("Day8/8_2.txt") as file:
        for line in file:
            arr.append(tuple( [int(x) for x in line.strip().split(',')] ))

    n = len(arr)
    h = []
    groups = []
    for i in range(n):
        for j in range(i+1,n):
            x1,y1,z1 = arr[i]
            x2,y2,z2 = arr[j]
            form = (x2-x1)**2+(y2-y1)**2+(z2-z1)**2
            heapq.heappush(h, (form, (i,j) ) )

    for _ in range(pairs):
        if h:
            smallest,pair = heapq.heappop(h)
            i,j = pair
            found = False
            for g in groups:
                if (i in g or j in g) and found == False:
                    g.add(i)
                    g.add(j)
                    found = True
                    addedGroup = g
                elif (i in g or j in g) and found == True:
                    groups.append(g.union(addedGroup))
                    if addedGroup in groups:
                        groups.remove(addedGroup)
                    if g in groups:
                        groups.remove(g)

            if found == False:
                newGroup = set()
                newGroup.add(i)
                newGroup.add(j)
                groups.append(newGroup)

    groups = sorted(groups, key=len,reverse=True)
    res = 1
    for i in range(3):
        if len(groups) > i:
            res *= len(groups[i])
    return res

def dayEight2():
    arr = []
    #read
    with open("Day8/8_2.txt") as file:
        for line in file:
            arr.append(tuple( [int(x) for x in line.strip().split(',')] ))

    n = len(arr)
    h = []
    groups = []
    for i in range(n):
        for j in range(i+1,n):
            x1,y1,z1 = arr[i]
            x2,y2,z2 = arr[j]
            form = (x2-x1)**2+(y2-y1)**2+(z2-z1)**2
            heapq.heappush(h, (form, (i,j) ) )

    while True:
        if h:
            smallest,pair = heapq.heappop(h)
            i,j = pair
            found = False
            for g in groups:
                if (i in g or j in g) and found == False:
                    g.add(i)
                    g.add(j)
                    found = True
                    addedGroup = g
                elif (i in g or j in g) and found == True:
                    groups.append(g.union(addedGroup))
                    if addedGroup in groups:
                        groups.remove(addedGroup)
                    if g in groups:
                        groups.remove(g)

            if found == False:
                newGroup = set()
                newGroup.add(i)
                newGroup.add(j)
                groups.append(newGroup)

        if len(groups) == 1 and len(groups[0]) == len(arr):
            return arr[i][0]*arr[j][0]

def main():
    print("Hallo")
    print(dayEight(), "ist die Lösung von Teil 1")
    print(dayEight2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()