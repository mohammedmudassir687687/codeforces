def solve():
    n = int(input())
    x = 0
    tempList = []
    for i in range(n):
        tempList.append(input())
    for i in tempList:
        if '+' in i:
            x += 1
        else:
            x -= 1
    print(x)

solve()