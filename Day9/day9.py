from collections import deque
from typing import *

def dayNine():
    coord = []
    #read
    with open("Day9/9_2.txt") as file:
        for line in file:
            j,i = [int(x) for x in line.strip().split(',')]
            coord.append( (i,j) )

    n = len(coord)
    maxArea = 0
    for i in range(n):
        for j in range(i+1,n):
            x1,y1 = coord[i]
            x2,y2 = coord[j]
            area = abs(x1-x2+1)*abs(y1-y2+1)
            maxArea = max(maxArea,area)
    return maxArea

def dayNine2():
    coord = []

    #read
    with open("Day9/9_2.txt") as file:
        for line in file:
            j,i = [int(x) for x in line.strip().split(',')]
            coord.append( (i,j) )

    xs = sorted({x for x,_ in coord})
    ys = sorted({y for _,y in coord})

    grid = [ [0]*(len(ys)*2-1) for _ in range(len(xs)*2-1) ]
    m,n = len(grid),len(grid[0])
    #compress coords
    for (x1,y1),(x2,y2) in zip(coord,coord[1:]+coord[:1]):
        cx1,cx2 = sorted( [xs.index(x1)*2, xs.index(x2)*2] )
        cy1,cy2 = sorted( [ys.index(y1)*2, ys.index(y2)*2] )
        for cx in range(cx1,cx2+1):
            for cy in range(cy1,cy2+1):
                grid[cx][cy] = 1
    
    outside = {(-1,-1)}
    q = deque(outside)
    #flood fill
    while q:
        tx,ty = q.popleft()
        for nx,ny in [ (tx-1,ty),(tx+1,ty),(tx,ty-1),(tx,ty+1) ]:
            if nx < -1 or ny < -1 or nx > m or ny > n: continue
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1: continue
            if (nx,ny) in outside: continue
            outside.add( (nx,ny) )
            q.append( (nx,ny) )
    
    for x in range(m):
        for y in range(n):
            if (x,y) not in outside:
                grid[x][y] = 1

    #pre fix sum array
    psa = [ [0]*len(row) for row in grid ]
    for x in range(len(psa)):
        for y in range(len(psa[0])):
            left = psa[x-1][y] if x > 0 else 0
            top = psa[x][y-1] if y > 0 else 0
            topleft = psa[x-1][y-1] if x > 0 < y else 0
            psa[x][y] = left+top-topleft+grid[x][y]

    def valid(x1,y1,x2,y2):
        cx1,cx2 = sorted( [xs.index(x1)*2, xs.index(x2)*2] )
        cy1,cy2 = sorted( [ys.index(y1)*2, ys.index(y2)*2] )
        left = psa[cx1-1][cy2] if cx1 > 0 else 0
        top = psa[cx2][cy1-1] if cy1 > 0 else 0
        topleft = psa[cx1-1][cy1-1] if cx1 > 0 < cy1 else 0
        count = psa[cx2][cy2]-left-top+topleft
        return count == (cx2-cx1+1)*(cy2-cy1+1)
    
    rectArea = [(abs(x1-x2)+1)*(abs(y1-y2)+1) for i,(x1,y1) in enumerate(coord) for x2,y2 in coord[:i] if valid(x1,y1,x2,y2)]
    return max(rectArea)


def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()