import math

def solve():
    lb,bh,hl = map(int, input().split(' '))
    h = math.sqrt(hl*bh / lb)
    l = hl/h
    b = lb/l
    print(int(4*(l+b+h)))




solve()