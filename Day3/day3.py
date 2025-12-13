from typing import *

def dayThree():
    res = 0

    #read
    with open("Day3/3_2.txt") as file:
        for line in file:
            arr = [int(x) for x in line.strip()]
            n = len(arr)
            maxV = max(arr)
            secondLast = 0
            second = 0
            firstCase = False
            for i in range(n):
                if i < n-1:
                    secondLast = max(secondLast,arr[i])
                
                if firstCase:
                    second = max(second,arr[i])

                if arr[i] == maxV and i != n-1:
                    firstCase = True

            if firstCase:
                res += int(str(maxV)+str(second))
            else:
                res += int(str(secondLast)+str(maxV))
    return res

def dayThree2():
    res = 0

    #read
    with open("Day3/3_2.txt") as file:
        for line in file:
            jolts = ""
            arr = [int(x) for x in line.strip()]

            for index in range(11):
                digit = max(arr[:index-11])
                arr = arr[arr.index(digit)+1:]
                jolts += str(digit)

            jolts += str(max(arr))
            res += int(jolts)
    return res

def main():
    print("Hallo")
    print(dayThree(), "ist die Lösung von Teil 1")
    print(dayThree2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()