def solve():
    n = int(input())
    tempList = []
    mainList= []
    for i in range(n):
        tempList += map(int, input().split(' '))
        mainList.append(tempList)
        tempList = []

    totalLeftZeroes = 0
    totalRightZeroes = 0
    for i in mainList:
        if i[0] == 0:
            totalLeftZeroes += 1
        if i[1] == 0:
            totalRightZeroes += 1

    totalLeftOnes = n - totalLeftZeroes
    totalRightOnes = n - totalRightZeroes

    print(min(totalLeftZeroes, totalLeftOnes) + min(totalRightZeroes, totalRightOnes))
solve()