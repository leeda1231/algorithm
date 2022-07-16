T = int(input())
for _ in range(T):
    n = int(input())
    i = 0
    lst = []
    while n > 0:
        if n % 2 == 1:
            lst.append(i)
        n //= 2
        i += 1
    print(*lst)