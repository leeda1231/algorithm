c,n = map(int,input().split())
dp = [1e9]*(101+c)
ans = 1e9

for _ in range(n):
    cost, num = map(int,input().split())
    dp[num] = cost
    for i in range(num,101+c):
        dp[i] = min(dp[i], dp[i-num]+cost)

        if c <= i and dp[i] < ans:
            ans = dp[i]

print(ans)