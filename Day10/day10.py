import itertools
from typing import *

def dayTen():
    res = 0
    #read
    with open("Day10/10_2.txt") as file:
        for line in file:
            lights = set()
            buttons = []
            arr = line.rstrip().split(' ')

            for i,c in enumerate(arr[0]):
                if c == '#':
                    lights.add(i-1)
            
            for i in range(1,len(arr)-1):
                buttons.append( set([int(x) for x in arr[i][1:-1].split(',')]) )

            found = False
            for count in range(1,len(buttons)+1):
                for attempt in itertools.combinations(buttons,r=count):
                    tempLights = set()
                    for button in attempt:
                        tempLights ^= button
                    if tempLights == lights:
                        res += count
                        found = True
                        break
                if found:
                    break
    return res

def dayTen2():
    res = 0

    #read
    with open("Day10/10.txt") as file:
        for line in file:
            buttons = []
            jolts = []
            arr = line.rstrip().split(' ')
            for i in range(1,len(arr)-1):
                buttons.append( set([int(x) for x in arr[i][1:-1].split(',')]) )

            jolts = [int(x) for x in arr[-1][1:-1].split(',')]
            print(buttons,jolts)
            
    return res

def main():
    print("Hallo")
    #print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()