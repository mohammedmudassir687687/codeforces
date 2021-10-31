def solve():
    word = input()
    strList = []
    for ele in word:
        strList.append(ele)

    if strList[0] >= 'a' and strList[0] <= 'z':
        strList[0] = chr(ord(strList[0]) -32)
    word = ''.join(strList)

    print(word)

solve()