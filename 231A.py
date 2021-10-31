def solve():
    n = int(input())
    tempList = []
    mainList = []
    for i in range(n):
        tempList += map(int, input().split(' '))
        mainList.append(tempList)
        tempList = []


    cnt = 0
    sumCnt = 0
    for i in mainList:
        for j in i:
            if j == 1:
                cnt += 1
        if cnt >= 2:
            sumCnt += 1
        cnt = 0

    print(sumCnt)

solve()