# 재귀
def dfs(start):
    if len(ans) == 6:
        print(*ans)
        return
    for i in range(start,k):
        ans.append(s[i])
        dfs(i+1)
        ans.pop()

while 1:
    k,*s = map(int,input().split())
    if k == 0:
        break
    ans = []
    dfs(0)
    print()


# combinations
from itertools import combinations

while 1:
    k,*s = map(int,input().split())
    if k == 0:
        break
    for c in combinations(s,6):
        print(*c)
    print()