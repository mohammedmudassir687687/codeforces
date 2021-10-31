def solve():
    tempList = []
    tempList += map(int, input().split('+'))
    tempList.sort()
    for i in range(0, len(tempList)):
        if i == len(tempList) - 1:
            print(str(tempList[i]))
        else:
            print((str(tempList[i])), end='+')



solve()