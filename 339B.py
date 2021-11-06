def solve():
    n, m = map(int, input().split(' '))
    tempList = []
    tempList += map(int, input().split(' '))
    cur = 1
    time = 0
    for i in range(0, len(tempList)):
        if tempList[i] < cur:
            time += n + 1 - cur
            cur = 1
        time += tempList[i] - cur
        cur = tempList[i]
    print(time)
solve()