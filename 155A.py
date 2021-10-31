def solve():
    n = int(input())
    tempList = []
    tempList += map(int, input().split(' '))
    amazing = 0
    minimum = tempList[0]
    maximum = tempList[0]
    for i in tempList:
        if i < minimum:
            minimum = i
            amazing += 1
        elif i > maximum:
            maximum = i
            amazing += 1

    print(amazing)
solve()