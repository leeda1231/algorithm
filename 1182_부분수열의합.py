def dfs(start):
    global ans
    if len(p) == i:
        if sum(p) == s:
            ans += 1
        return
    for j in range(start,n):
        p.append(lst[j])
        dfs(j+1)
        p.pop()

n,s = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0
for i in range(1,n+1):
    p = []
    dfs(0)
print(ans)

# combinations
from itertools import combinations
n,s = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0

for i in range(1,n+1):
    for x in combinations(lst,i):
        if sum(x) == s:
            ans += 1
print(ans)