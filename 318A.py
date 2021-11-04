def solve():
    n, k = map(int, input().split(' '))
    if n % 2 == 0:
        if k > n / 2:
            print(int((2 * (k - n/2))))
        else:
            print(int(2*k - 1))
    else:
        if k < n // 2 + 2:
            print(int(2 * k - 1))
        else:
            print(int((k - (n//2+1))*2))
solve()
