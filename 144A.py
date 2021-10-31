def solve():
    swap = 0
    n = int(input())
    inputList = []
    inputList += map(int, input().split(' '))
    maxEl = max(inputList)
    minEl = min(inputList)
    maxPosition = -1
    minPosition = -1
    for i in range(0, len(inputList)):
        if inputList[i] == maxEl:
            maxPosition = i
            break
    for i in range(len(inputList) - 1, -1, -1):
        if inputList[i] == minEl:
            minPosition = i
            break

    if maxPosition <= minPosition:
        swap += maxPosition
        swap += len(inputList) - 1 - minPosition
    else:
        swap += maxPosition
        swap += len(inputList) - 1 - minPosition
        swap -= 1
    print(swap)
solve()