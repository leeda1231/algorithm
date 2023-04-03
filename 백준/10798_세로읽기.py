arr = []
m = 0
for _ in range(5):
    lst = list(input())
    if len(lst) > m:
        m = len(lst)
    arr.append(lst)

ans = ''
for j in range(m):
    for i in range(5):
        try:
            ans += arr[i][j]
        except:
            continue
print(ans)