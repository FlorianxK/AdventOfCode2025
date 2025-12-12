from typing import *

def dayTwo(): 
    arr = []
    #read
    with open("Day2/2_2.txt") as file:
        for line in file:
           arr = line.strip().split(',')

    res = 0
    for a in arr:
        l,r = [int(x) for x in a.split('-')]
        for i in range(l,r+1):
            word = str(i)
            mid = len(word)//2
            if word[:mid] == word[mid:]:
                res += i
    return res

def dayTwo2():
    arr = []
    #read
    with open("Day2/2_2.txt") as file:
        for line in file:
           arr = line.strip().split(',')

    def invalid(word:str):
        n = len(word)
        res = False
        for i in range(1, n//2+1):
            if n%i == 0:
                if word[:i] * (n//i) == word:
                    res = True
                    break
        return res

    res = 0
    for a in arr:
        l,r = [int(x) for x in a.split('-')]
        for i in range(l,r+1):
            word = str(i)

            if invalid(word):
                res += i

    return res

def main():
    print("Hallo")
    print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()