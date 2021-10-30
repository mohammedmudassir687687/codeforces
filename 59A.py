def solve():
    s = input()
    strList = []
    for ele in s:
        strList.append(ele)

    cntUpperCase = 0
    cntLowerCase = 0
    for i in strList:
        if i >= 'A' and i <= 'Z':
            cntUpperCase += 1
        else:
            cntLowerCase += 1

    if cntUpperCase > cntLowerCase:
        cntUpperCase = True
    else:
        cntUpperCase = False

    if cntUpperCase:
        for i in range(0, len(strList)):
            if strList[i] >= 'a' and strList[i] <= 'z':
                strList[i] = chr(ord(strList[i]) - 32)
    else:
        for i in range(0, len(strList)):
            if strList[i] >= 'A' and strList[i] <= 'Z':
                strList[i] = chr(ord(strList[i]) + 32)


    s = ''.join(strList)
    print(s)
solve()