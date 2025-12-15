from collections import deque
from functools import cache
from typing import *

def daySeven():
    splitter = 0
    arr = []
    start = ()
    i = 0
    #read
    with open("Day7/7_2.txt") as file:
        for line in file:
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
            arr.append(list(line.strip()))
            i += 1
    m,n = len(arr),len(arr[0])
    seen = set()
    seen.add(start)
    q = deque([start])
    while q:
        i,j = q.popleft()
        i += 1
        if 0<=i<m and 0<=j<n and (i,j) not in seen:
            seen.add( (i,j) )
            if arr[i][j] == '.':
                arr[i][j] = '|'
                q.append( (i,j) )
            elif arr[i][j] == '^':
                splitter += 1
                for dx,dy in [(0,-1),(0,1)]:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in seen:
                        seen.add( (nx,ny) )
                        arr[nx][ny] = '|'
                        q.append( (nx,ny) )
    return splitter

def daySeven2():
    arr = []
    start = ()
    i = 0
    #read
    with open("Day7/7_2.txt") as file:
        for line in file:
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
            arr.append(list(line.strip()))
            i += 1
    m,n = len(arr),len(arr[0])

    @cache
    def solve(i,j):
        if i >= m: return 1

        if arr[i][j] == '.' or arr[i][j] == 'S':
            return solve(i+1,j)
        elif arr[i][j] == '^':
            return solve(i,j-1) + solve(i,j+1)

    return solve(*start)

def main():
    print("Hallo")
    print(daySeven(), "ist die Lösung von Teil 1")
    print(daySeven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()