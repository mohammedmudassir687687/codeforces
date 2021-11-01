def solve():

    numOfElements = int(input())
    numList = input().split(' ')

    numofQueries = int(input())
    queriesList = input().split(' ')


    totalVasya = 0
    totalPetya = 0

    for q in queriesList:
        i = numList.index(q)
        totalVasya += i + 1
        totalPetya += numOfElements - i

    print(totalVasya, totalPetya)
solve()