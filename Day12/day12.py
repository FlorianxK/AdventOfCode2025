from typing import *

def dayEleven():
    res = 0
    forms = []
    first = True
    #read
    with open("Day12/12_2.txt") as file:
        for line in file:
            line = line.rstrip()
            if 'x' in line:
                first = False

            if first:
                if ':' in line:
                    index = 0
                    newForm = []
                elif line == '':
                    forms.append(newForm)
                else:
                    for j in range(len(line)):
                        if line[j] == '.':
                            newForm.append( (index,j) )
                    index += 1
            else:
                l,r = line.split(': ')
                x,y = [int(v) for v in l.split('x')]
                arr = [int(v) for v in r.split(' ')]
                if (x//3)*(y//3) >= sum(arr):
                    res += 1
    return res

def main():
    print("Hallo")
    print(dayEleven(), "ist die Lösung")
     
if __name__=="__main__":
    main()