def solve():
    tempList = []
    tempList += map(int, input().split(' '))
    seen = []
    notSeenCnt = 0
    # seen, not seen
    # no. of different integers
    # 4 - no. of different integers

    for i in tempList:
        if i not in seen:
            seen.append(i)
            notSeenCnt += 1

    print(4 - notSeenCnt)



solve()