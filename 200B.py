def solve():
    n = int(input())
    tempList = []
    tempList += map(int, input().split(' '))
    sum = 0
    for i in tempList:
        sum += i
    print(sum/n)
solve()