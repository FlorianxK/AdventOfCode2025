from collections import defaultdict, deque
from functools import cache
from typing import *

def dayEleven():
    res = 0
    d = defaultdict(list)
    #read
    with open("Day11/11_2.txt") as file:
        for line in file:
            l,r = line.rstrip().split(': ')
            d[l].extend(r.split(' '))

    queue = deque(["you"])
    
    while queue:
        curr = queue.popleft()

        for nxt in d[curr]:
            if nxt == "out":
                res += 1
            else:
                queue.append(nxt)
    return res

def dayEleven2():
    d = defaultdict(list)
    #read
    with open("Day11/11_2.txt") as file:
        for line in file:
            l,r = line.rstrip().split(': ')
            d[l].extend(r.split(' '))

    @cache
    def solve(src,dst):
        if src == dst:
            return 1
        arr = [solve(x,dst) for x in d.get(src,[])]
        return sum( arr )
    
    first = solve("svr","dac")*solve("dac","fft")*solve("fft","out")
    second = solve("svr","fft")*solve("fft","dac")*solve("dac","out")
    
    return first+second

def main():
    print("Hallo")
    print(dayEleven(), "ist die Lösung von Teil 1")
    print(dayEleven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()