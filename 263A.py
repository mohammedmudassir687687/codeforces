def solve():
    tempList = []
    mainList = []
    x = y = 0
    locationi = locationj = 0
    for i in range(5):
            tempList += map(int, input().split(' '))
            for j in range(5):
                if tempList[j] == 1:
                    locationi, locationj = i, j
            mainList.append(tempList)
            tempList = []

    x,y = abs(2-locationi), abs(2-locationj)

    print(x+y)


solve()























