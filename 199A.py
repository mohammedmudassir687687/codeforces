def solve():

    n = int(input())
    a = 0
    b = 1
    tempb = b
    tempa = a
    sum = 0
    if n == 0:
        print('0 0 0')
        return 0
    elif n == 1:
        print('0 0 1')
        return 0
    elif n == 2:
        print('0 1 1')
        return 0
    else:
        while(sum != n):
            #temp = b
            sum = a + b
            if sum == n:
                break
            c = a
            a = b
            b = sum



    print(c, a, a)



solve()