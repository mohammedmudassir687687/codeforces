def solve():
    n = int(input())
    tempList = []
    mainList = []
    for i in range(n):
        tempList += map(int, input().split(' '))
        mainList.append(tempList)
        tempList = []


    superCentral = []
    for point in mainList:
        checkAbove = False
        checkBelow = False
        checkRight = False
        checkLeft = False
        # in i except this point
        # x should be same but y value should be more and less than y value of this point
        # y should be same but x value should be more and less than x value of this point
        # if above conditions satisfy add this to superCentral

        for i in range(0, len(mainList)):

            if point[0] == mainList[i][0] and point[1] < mainList[i][1]:
                checkAbove = True
            elif point[0] == mainList[i][0] and point[1] > mainList[i][1]:
                checkBelow = True
            elif point[1] == mainList[i][1] and point[0] < mainList[i][0]:
                checkRight = True
            elif point[1] == mainList[i][1] and point[0] > mainList[i][0]:
                checkLeft = True
            #print(check)
            if checkAbove and checkLeft and checkBelow and checkRight:
                if point not in superCentral:
                    superCentral.append(point)

    print(len(superCentral))

solve()