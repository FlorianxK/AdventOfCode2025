from typing import *

def dayFive():
    res = 0
    arr = []

    def overlap(arr):
        newArr = [arr[0]]
        for i in range(1,len(arr)):
            if arr[i][0] <= newArr[-1][1]:
                old = newArr.pop()
                newArr.append( (old[0], max(old[1], arr[i][1])) )
            else:
                newArr.append(arr[i])
        return newArr
    
    def bs(val):
        l,r = 0,len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid][0] <= val <= arr[mid][1]:
                return True
            elif val > arr[mid][1]:
                l = mid+1
            elif val < arr[mid][0]:
                r = mid-1

        return False

    #read
    first = True
    with open("Day5/5_2.txt") as file:
        for line in file:
            if line == '\n':
                arr.sort()
                arr = overlap(arr)
                first = False
                continue

            if first:
                line = line.strip()
                l,r = [int(x) for x in line.split('-')]
                arr.append( (l,r) )
            else:
                v = int(line)
                if bs(v):
                    res += 1
    return res

def dayFive2():
    res = 0
    arr = []

    def overlap(arr):
        newArr = [arr[0]]
        for i in range(1,len(arr)):
            if arr[i][0] <= newArr[-1][1]:
                old = newArr.pop()
                newArr.append( (old[0], max(old[1], arr[i][1])) )
            else:
                newArr.append(arr[i])
        return newArr

    #read
    with open("Day5/5_2.txt") as file:
        for line in file:
            if line == '\n':
                arr.sort()
                arr = overlap(arr)
                for l,r in arr:
                    res += r-l+1
                return res

            line = line.strip()
            l,r = [int(x) for x in line.split('-')]
            arr.append( (l,r) )



def main():
    print("Hallo")
    print(dayFive(), "ist die Lösung von Teil 1")
    print(dayFive2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()