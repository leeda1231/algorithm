# 1
from itertools import combinations

T = int(input())
for tc in range(T):
    n,b = map(int,input().split())
    h = list(map(int,input().split()))
    lst = []
    for i in range(1,n+1):
        for x in combinations(h,i):
            lst.append(sum(x))
    lst.sort()
    for l in lst:
        if l >= b:
            ans = l-b
            break
    print(f'#{tc+1}',ans)

# 2
T = int(input())
 
def dfs(n,x):
    global ans
    # 가지치기 => 실행시간이 반드시 줄어드는 것은 아님. 상황에 따라 다르다.
    if x >= B + ans:
        return
    if n == N:
        if x >= B and x-B < ans:
            ans = x - B
        return
    dfs(n+1,x+h[n])
    dfs(n+1,x)
     
for tc in range(T):
    N,B = map(int,input().split())
    h = list(map(int,input().split()))
    ans = 200000
    dfs(0,0)
    print(f'#{tc+1}',ans)