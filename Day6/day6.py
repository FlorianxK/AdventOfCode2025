from typing import *

def daySix():
    res = 0
    arr = []

    #read
    with open("Day6/6_2.txt") as file:
        for line in file:
            arr.append(line.strip().split())

    m,n = len(arr),len(arr[0])
    for j in range(n):
        op = arr[-1][j]
        if op == '+':
            tempRes = 0
            for i in range(m-1):
                tempRes += int(arr[i][j])
        elif op == '*':
            tempRes = 1
            for i in range(m-1):
                tempRes *= int(arr[i][j])

        res += tempRes
    return res

def daySix2():
    res = 0
    arr = []
    n = 0
    #read
    with open("Day6/6_2.txt") as file:
        for line in file:
            line = line.rstrip()
            n = max(n,len(line))
            arr.append(list(line))
    for a in arr:
        if len(a) < n:
           a.extend([' ']*(n-len(a)))

    m = len(arr)
    vals = []
    res = 0
    skip = False
    for j in range(n-1,-1,-1):
        word = ""
        for i in range(m):
            if arr[i][j] == '+':
                vals.append(int(word))
                tempRes = 0
                for v in vals:
                    tempRes += v

                res += tempRes
                vals = []
                skip = True
                continue

            elif arr[i][j] == '*':
                vals.append(int(word))
                tempRes = 1
                for v in vals:
                    tempRes *= v
                
                res += tempRes
                vals = []
                skip = True
                continue

            elif arr[i][j] != ' ':
                word += arr[i][j]

        if skip == False:
            if word:
                vals.append(int(word))
        else:
            skip = False
    return res

def main():
    print("Hallo")
    print(daySix(), "ist die Lösung von Teil 1")
    print(daySix2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()