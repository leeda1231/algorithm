n = int(input())
ans = 0
for k in range(1,n):
    total = k
    q = k
    while k:
        total += k%10
        k//=10
    if total == n:
        ans = q
        break
print(ans)