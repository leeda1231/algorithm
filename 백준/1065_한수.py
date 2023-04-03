n = int(input())

def f(n):
    x = n % 10
    n //= 10
    y = n % 10
    z = n // 10
    if (x-y) == (y-z):
        return 1
    return 0


if n < 100:
    print(n)
else:
    ans = 99
    for i in range(100,n+1):
        ans += f(i)
    print(ans)