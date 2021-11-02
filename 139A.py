def solve():
    n = int(input())
    tempList = []
    tempList += map(int, input().split(' '))

    flag = True
    while(flag):
        for i in range(0, len(tempList)):
            if n > 0:
                n = n-tempList[i]
                if n <= 0:
                    print(i + 1)
                    flag = False
                    break
            else:
                print(i + 1)
                flag = False
                break




solve()