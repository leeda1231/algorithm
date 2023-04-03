N, M = map(int,input().split())
lst = list(map(int,input().split()))

s = 0
e = 1
cnt = 0

while s <= e and e <= N:
    if sum(lst[s:e]) < M:
        e += 1
    elif sum(lst[s:e]) == M:
        cnt += 1
        s += 1
        e += 1
    elif sum(lst[s:e]) > M:
        s += 1

print(cnt)