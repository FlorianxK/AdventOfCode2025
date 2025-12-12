from typing import *

def dayOne():
    res = 0
    dial = 50
    
    #read
    with open("Day1/1_2.txt") as file:
        for line in file:
            direction,move = line[0],int(line[1:])
            if direction == 'L':
                move *= -1
            dial = (dial+move)%100
            if dial == 0:
                res += 1
    return res

def dayOne2():
    res = 0
    dial = 50
    #read
    with open("Day1/1_2.txt") as file:
        for line in file:
            direction,move = line[0],int(line[1:])
            if direction == 'L':
                move *= -1
            
            if move < 0:
                v = -100
                res += move//v
                if dial != 0 and dial + move%v <= 0:
                    res += 1
            else:
                v = 100
                res += move//v
                if dial + move%v >= 100:
                    res += 1
            
            dial = (dial+move)%100

    return res

def main():
    print("Hallo")
    print(dayOne(), "ist die Lösung von Teil 1")
    print(dayOne2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()