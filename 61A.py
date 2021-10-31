def solve():
    num1 = input()
    num2 = input()
    num1List = []
    num2List = []
    for ele1 in num1:
        num1List.append(ele1)
    for ele2 in num2:
        num2List.append(ele2)

    for i in range(0,len(num1List)):
        if num1List[i] == num2List[i]:
            num1List[i] = '0'
        else:
            num1List[i] = '1'

    print(''.join(num1List))


solve()