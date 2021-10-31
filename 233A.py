def solve():
    n = int(input())
    tempList = []
    if n % 2 == 1:
        print(-1)
        return 0
    else:
        i = 1
        while i < n:
            tempList.append(str(i+1)+' ')
            tempList.append(str(i)+' ')
            i += 2
    s = ''.join(tempList)
    print(s)
solve()