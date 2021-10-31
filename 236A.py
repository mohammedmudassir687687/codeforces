def solve():
    username = input()
    tempList = list(username)
    cnt = 0
    seen = []
    #seen, not seen
    #add count if not seen before
    for i in tempList:
        if i not in seen:
            seen.append(i)
            cnt += 1

    if cnt % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')

solve()