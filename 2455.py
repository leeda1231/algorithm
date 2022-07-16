total = 0
ans = 0
for i in range(4):
    x, y = map(int,input().split())
    total = total - x + y
    if total > ans:
        ans = total
print(ans)