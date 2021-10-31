def solve():
    cur = 0
    maximum = 0

    n = int(input())
    singleStop = []
    allStops = []
    for i in range(n):
        singleStop += map(int, input().split(' '))
        allStops.append(singleStop)
        singleStop = []

    for i in range(n):
        cur += allStops[i][1] - allStops[i][0]
        maximum = max(cur, maximum)

    print(maximum)
solve()