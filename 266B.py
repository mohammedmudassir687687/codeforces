def solve():
    n, t = map(int, input().split(' '))
    s = input()
    inputList = list(s)
    flag = False

    j = 0
    for i in range(t):
        while j < n:
            if flag:
                j += 2
            if j+1 < len(inputList) and inputList[j] == 'B' and inputList[j+1] == 'G':
                temp = inputList[j]
                inputList[j] = inputList[j+1]
                inputList[j+1] = temp
                flag = True
            else:
                flag = False
                j += 1
        j = 0


    s = ''.join(inputList)
    print(s)

solve()