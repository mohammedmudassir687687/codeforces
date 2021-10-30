def solve():
    n = int(input())
    sumX = 0
    sumY = 0
    sumZ = 0
    list = []
    tempList = []
    for i in range(0,n):
        x, y, z = map(int, input().split(' '))
        tempList.append(x)
        tempList.append(y)
        tempList.append(z)
        list.append(tempList)
        tempList = []
    for i in list:
        sumX += i[0]
        sumY += i[1]
        sumZ += i[2]
    if sumX == 0 and sumY == 0 and sumZ == 0:
        print('YES')
    else:
        print('NO')
solve()