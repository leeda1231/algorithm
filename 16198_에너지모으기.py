n = int(input())
w = list(map(int,input().split()))
ans = 0
def dfs(w,e):
    global ans
    if len(w) == 2:
        ans = max(ans,e)
    for i in range(1,len(w)-1):
        dfs(w[:i]+w[i+1:],e+w[i-1]*w[i+1])

dfs(w,0)
print(ans)