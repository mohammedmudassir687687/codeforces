def solve():
    n = int(input())
    tempList = []
    tempList += map(int, input().split(' '))

    pairI, pairJ = 0, 0
    min = max(tempList)
    for i in range(0, len(tempList)-1):
        j = i+1
        if min > abs(tempList[i] - tempList[j]):
            min = abs(tempList[i] - tempList[j])
            pairI = i+1
            pairJ = j+1

    if min > abs(tempList[0] - tempList[len(tempList) - 1]):
        pairI = 1
        pairJ = len(tempList)
    print(pairI, pairJ)
solve()