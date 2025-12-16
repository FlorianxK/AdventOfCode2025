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
    allowed = set()
    maxI,maxJ = 0,0
    #read
    with open("Day9/9.txt") as file:
        for line in file:
            j,i = [int(x) for x in line.strip().split(',')]
            coord.append( (i,j) )
            allowed.add( (i,j) )
            maxI = max(maxI,i)
            maxJ = max(maxJ,j)
    n = len(coord)

    arr = [ ['.']*(maxJ+3) for _ in range(maxI+2) ]
    for i,j in coord:
        arr[i][j] = '#'

    start = ()
    n = len(coord)
    for i in range(n):
        for j in range(i+1,n):
            x1,y1 = coord[i]
            x2,y2 = coord[j]
            
            if x1 == x2:
                big = max(y1,y2)
                small = min(y1,y2)
                for k in range(small+1,big):
                    if start == ():
                        start = (x1,k)
                    arr[x1][k] = 'X'
            elif y1 == y2:
                big = max(x1,x2)
                small = min(x1,x2)
                for k in range(small+1,big):
                    if start == ():
                        start = (k,y1)
                    arr[k][y1] = 'X'

    #fill inside without arr
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    inside = False
    for dx,dy in directions:
        s1,s2 = start[0]+dx,start[1]+dy

        for fullx,fully in directions:
            inside = True
            nx,ny = s1,s2
            while True:
                nx,ny = nx+fullx,ny+fully

                if 0<=nx<maxI+1 and 0<=ny<maxJ+1:
                    if (nx,ny) in coord:
                        print("found")
                        break
                else:
                    inside = False
                    break

            if inside == False:
                break
    
    print(nx,ny)
            
    #check if all 4 corners are in allowed
    # x1,y1 x2,y1 x1,y2, x2,y2

def main():
    print("Hallo")
    #print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()