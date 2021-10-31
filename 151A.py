def solve():
    n, k, l, c, d, p, nl, np = map(int, input().split(' '))

    totalDrink = k*l
    totalLimeSlices = c*d
    totalSalt = p

    numberOfDrinks = totalDrink // (n * nl)
    numberOfSlices = c * d // n
    numberOfSalt = p // (n * np)

    print(min(numberOfSalt, numberOfSlices, numberOfDrinks))

solve()
