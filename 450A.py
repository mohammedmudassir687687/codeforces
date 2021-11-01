import math
def solve():
    n, m = map(int, input().split(' '))

    tempList = []
    tempList += map(int, input().split(' '))

    maximum = max(tempList)
    cntValid = n
    while(True):
        i = 0
        while i < len(tempList):
            if cntValid == 1 and tempList[i] > 0:
                print(i+1)
                return 0
            elif tempList[i] > 0:
                tempList[i] -= m
                if tempList[i] < 1:
                    cntValid -= 1
            i += 1
solve()