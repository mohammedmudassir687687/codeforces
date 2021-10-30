def solve():
    givenYear = int(input()) + 1
    while(True):
        thousandsDigit = givenYear//1000
        hundredsDigit = (givenYear%1000)//100
        tensDigit = (givenYear%100)//10
        onesDigit = (givenYear%10)

        if thousandsDigit != hundredsDigit and thousandsDigit != tensDigit and thousandsDigit != onesDigit and \
                hundredsDigit != tensDigit and hundredsDigit != onesDigit and tensDigit != onesDigit:
            print(givenYear)
            return 0
        else:
            givenYear += 1

solve()