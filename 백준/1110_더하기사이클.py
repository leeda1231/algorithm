n = int(input())

def cycle(n):
    a = n//10
    b = n%10
    x = 10*b + (a+b)%10
    return x

ans = n
cnt = 0
while 1:
    cnt += 1
    n = cycle(n)
    if ans == n:
        break
print(cnt)