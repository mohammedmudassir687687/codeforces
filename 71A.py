def solve():
    n = int(input())
    words = []
    modifiedWords = []
    for i in range(n):
        words.append(input())

    for i in words:
        if len(i) <= 10:
            modifiedWords.append(i)
        else:
            newWord = i[0] + str(len(i) - 2) + i[len(i) - 1]
            modifiedWords.append(newWord)

    for i in modifiedWords:
        print(i)

solve()