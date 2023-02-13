T = int(input())
for _ in range(T):
    s = input()
    tmp = 'X'
    cnt = 0
    total = 0
    for x in s:
        if x == 'O':
            if tmp == 'X':
                tmp = 'O'
            cnt += 1
            total += cnt
        else:
            tmp = 'X'
            cnt = 0
    print(total)
