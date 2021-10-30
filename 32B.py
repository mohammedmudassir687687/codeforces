def solve():
    s = input()
    listS = []
    for ele in s:
        listS.append(ele)

    res = ''

    i = 0
    while i < len(listS):
        if listS[i] == '.':
            res = res + '0'
            i += 1
        elif listS[i] == '-':
            if i+1 < len(listS) and listS[i+1] == '.':
                res = res + '1'
                i += 2
            elif i+1 < len(listS) and listS[i] == '-':
                res = res + '2'
                i += 2
    print(res)

solve()
