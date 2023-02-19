
#1
def new_blackjack(n,m):
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                x = lst[i] + lst[j] + lst[k]
                if x <= m and x > ans:
                    print(i,j,k)
                    ans = x
    return ans

n,m = map(int,input().split())
lst = list(map(int,input().split()))
print(new_blackjack(n,m))

#2
from itertools import combinations

n,m = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0
for c in combinations(lst,3):
    s = sum(c)
    if s <= m and s > ans:
        ans = s
print(ans)