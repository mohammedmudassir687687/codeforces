def solve():
    str1 = input().lower()
    str2 = input().lower()
    for i in range(0,len(str1)):
        if str1[i] < str2[i]:
            print(-1)
            return 0
        elif str1[i] > str2[i]:
            print(1)
            return 0
    print(0)
solve()