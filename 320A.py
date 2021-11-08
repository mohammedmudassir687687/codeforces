def solve():
    n = input()
    tempList = []
    for ele in n:
        tempList.append(ele)

    countOfFour = 0
    if tempList[0] != '1':
        print('NO')
        return 0
    for i in range(1, len(tempList)):
        if tempList[i] == '4':
            countOfFour += 1
            if countOfFour > 2:
                print('NO')
                return 0
        elif tempList[i] == '1':
            countOfFour = 0
        else:
            print('NO')
            return 0

    print('YES')
solve()