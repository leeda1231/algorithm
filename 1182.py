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