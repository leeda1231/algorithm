x = int(input())
n = 1
gap = 2
while 1:
    if x <= n:
        if gap%2 == 0:
            u = n-x+1
            d = (gap-1)-(n-x)
        else:
            u = (gap-1)-(n-x)
            d = n-x+1
        print(f'{u}/{d}')
        break
    n += gap
    gap += 1