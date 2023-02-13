# dp
T = int(input())
for tc in range(T):
    d,m,q,y = map(int,input().split())
    plans = [0] + list(map(int,input().split()))
    dp = [0] + [y]*12
    for i in range(1,13):
        if i < 3:
            dp[i] = min(dp[i],dp[i-1]+m,dp[i-1]+d*plans[i])
        else:
            dp[i] = min(dp[i],dp[i-1]+m,dp[i-1]+d*plans[i],dp[i-3]+q)
    print(f'#{tc+1}',dp[12])


# dfs
def dfs(n,total):
    global ans
    if n >= 12:
        if ans > total:
            ans = total
        return
    dfs(n+1,total+d*plans[n])
    dfs(n+1,total+m)
    dfs(n+3,total+q)

T = int(input())
for tc in range(T):
    d,m,q,ans = map(int,input().split())
    plans = list(map(int,input().split()))
    dfs(0,0)
    print(f'#{tc+1}',ans)
