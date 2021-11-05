def solve():
    n = int(input())
    tempList = []
    tempList += map(int, input().split(' '))
    if tempList.count(min(tempList)) == 1:
        print(tempList.index(min(tempList)) + 1)
    else:
        print('Still Rozdil')
solve()