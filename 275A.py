matrix = [[1,1,1],[1,1,1],[1,1,1]]

def solve():
    inputList = []
    mainList = []
    for i in range(3):
        inputList += map(int, input().split(' '))
        mainList.append(inputList)
        inputList = []

    for i in range(3):
        for j in range(3):
            if mainList[i][j] != 0:
                while mainList[i][j]:
                    toggle(i,j)

                    if i-1 > -1:
                        toggle(i-1,j)
                    if i+1 < 3:
                        toggle(i+1,j)
                    if j-1>-1:
                        toggle(i,j-1)
                    if j+1<3:
                        toggle(i,j+1)

                    mainList[i][j] -= 1

    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end='')
        print()

def toggle(i,j):
    if matrix[i][j] == 0:
        matrix[i][j] = 1
    elif matrix[i][j] == 1:
        matrix[i][j] = 0

solve()