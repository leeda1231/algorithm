n,l = map(int,input().split())
pools = [list(map(int,input().split())) for _ in range(n)]
pools.sort()
cnt = 0
end = 0
tmp = pools[0][0]

for i in range(n):
    if end >= pools[i][1]:
        continue
    elif end > pools[i][0]:
        d = pools[i][1] - end
    else:
        d = pools[i][1] - pools[i][0]
    cnt += d // l
    if d % l:
        cnt += 1
        end = pools[i][1] + l - (d % l)

print(cnt)