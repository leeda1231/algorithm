n = int(input())
dp = list(map(int,input().split()))
for i in range(1,n):
    dp[i] = max(dp[i], dp[i-1] + dp[i])

for i in range(n):
    pass