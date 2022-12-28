T = int(input())
for _ in range(T):
    x,*lst = input().split()
    x = float(x)
    for l in lst:
        if l == '@':
            x *= 3
        elif l == '%':
            x += 5
        else:
            x -= 7
    print('%.2f'%x)