def solve():
    name1 = list(input())
    name2 = list(input())
    pile = list(input())


    if (len(name1) + len(name2)) != len(pile):
        print('NO')
        return 0
    else:
        newName = name1 + name2
        newName.sort()
        pile.sort()
        for i in range(0, len(newName)):
            if newName[i] != pile[i]:
                print('NO')
                return 0
    print('YES')
solve()