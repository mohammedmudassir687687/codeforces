def solve():
    n = int(input())
    word = input()
    updateCount = 0
    wordList = []
    for ele in word:
        wordList.append(ele)

    # seenElement, curElement
    curElement = seenElement = wordList[0]
    # iterate and update the seenElement if curElement is different and increase updateCount if it is same element
    for i in range(1, len(wordList)):
        curElement = wordList[i]
        if curElement != seenElement:
            seenElement = curElement
        else:
            updateCount += 1

    print(updateCount)
solve()