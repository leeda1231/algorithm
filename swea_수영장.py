T = int(input())

# dp
for tc in range(T):
    d,m,q,y = map(int,input().split())
    plan = [0] + list(map(int,input().split()))
    dp = [0] + [y] * 12
    for i in range(1,13):
        if i < 3:
            dp[i] = min(dp[i], dp[i-1] + d*plan[i], dp[i-1] + m)
        else:
            dp[i] = min(dp[i], dp[i-1] + d*plan[i], dp[i-1] + m, dp[i-3] + q)
    print(f'#{tc+1} {dp[12]}')

'''
# dfs
def dfs(n,pay):
    global ans
    if n > 12:
        if pay < ans:
            ans = pay
        return
    dfs(n+1, pay+plan[n]*d)
    dfs(n+1, pay+m)
    dfs(n+3, pay+q)
    
for tc in range(T):
    d,m,q,y = map(int,input().split())
    plan = [0] + list(map(int,input().split()))
    ans = y
    dfs(1,0)
    print(f'#{tc+1} {ans}')
'''