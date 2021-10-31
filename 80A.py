import math
def solve():
    x,y = map(int, input().split(' '))
    flag = False
    temp = x
    while(True):
        temp += 1
        for i in range(2, temp):
            if temp % i == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            break
    if y == 3 or temp == y:
        print('YES')
    else:
        print('NO')

solve()