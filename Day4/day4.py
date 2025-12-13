from typing import *

def dayFour():
    res = 0
    arr = []
    #read
    with open("Day4/4_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))

    m,n = len(arr),len(arr[0])
    for i in range(m):
        for j in range(n):
            if arr[i][j] != '@': continue

            nxt = 0
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]:
                nx,ny = i+dx,j+dy
                if 0<=nx<m and 0<=ny<n:
                    if arr[nx][ny] == '@':
                        nxt += 1

                if nxt >= 4:
                    break
            
            if nxt < 4:
                res += 1
    return res

def dayFour2():
    arr = []
    #read
    with open("Day4/4_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))

    def oneRound():
        lRes = 0
        m,n = len(arr),len(arr[0])
        for i in range(m):
            for j in range(n):
                if arr[i][j] != '@': continue

                nxt = 0
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n:
                        if arr[nx][ny] == '@':
                            nxt += 1

                    if nxt >= 4:
                        break
                
                if nxt < 4:
                    arr[i][j] = '.'
                    lRes += 1
        return lRes

    res = 0
    while True:
        v = oneRound()
        if v == 0:
            break
        else:
            res += v
    return res

def main():
    print("Hallo")
    print(dayFour(), "ist die Lösung von Teil 1")
    print(dayFour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()