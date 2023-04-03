n,k = map(int,input().split())

ans = 0
cnt = 0
i = 0

while cnt < k:
    if i > n:
        ans = 0
        break
    # if cnt == k:
    #     break
    i += 1
    if n % i == 0:
        cnt += 1
        ans = i

print(ans)