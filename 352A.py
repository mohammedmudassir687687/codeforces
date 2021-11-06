def solve():
    n = int(input())
    tempList = []
    tempList += map(int, input().split(' '))

    if tempList.count(0) == 0:
        print(-1)
        return
    if tempList.count(5) < 9:
        print(0)
        return
    res = []
    countOfFive = tempList.count(5)
    remainder = countOfFive % 9
    if countOfFive >= 9:
        for i in range(countOfFive - remainder):
            res.append(str(5))

    countOfZeroes = tempList.count(0)
    for i in range(countOfZeroes):
        res.append(str(0))

    print(''.join(res))





solve()