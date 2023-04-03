n = int(input())
ans = 0
for _ in range(n):
    a,b,c = map(int,input().split())
    if a == b == c:
        val = 10000 + 1000 * a
    elif a == b:
        val = 1000 + 100 * a
    elif b == c:
        val = 1000 + 100 * b
    elif a == c:
        val = 1000 + 100 * a
    else:
        val = 100 * max(a,b,c)
    if val > ans:
        ans = val

print(ans)