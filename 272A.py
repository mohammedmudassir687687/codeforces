def solve():
    numOfFriends = int(input())
    fingerCount = []
    fingerCount += map(int, input().split(' '))
    totalFingers = 0
    for i in fingerCount:
        totalFingers += i


    ways = 0
    for dima in range(1, 6):
        if (totalFingers + dima) % (numOfFriends + 1) != 1:
            ways += 1

    print(ways)
solve()