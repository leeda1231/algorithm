from pprint import pprint

n = int(input())
dp = [[1]*10] + [[0]*10 for _ in range(n-1)]
if n != 1:
    for j in range(10):
        dp[1][j] = 10-j

for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i][j] = sum(dp[i-1])
            continue
        dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

pprint(dp)
print(sum(dp[-1]) % 10007)