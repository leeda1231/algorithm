n = int(input())
int_tri = []
for _ in range(n):
    int_tri.append(list(map(int,input().split())))

dp = [[0]*i for i in range(1,n+1)]
dp[0][0] = int_tri[0][0]

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + int_tri[i][j]
            continue
        if j == i:
            dp[i][j] = dp[i-1][j-1] + int_tri[i][j]
            continue
        dp[i][j] = max(dp[i-1][j-1] + int_tri[i][j], dp[i-1][j] + int_tri[i][j])

print(dp)
print(max(dp[n-1]))
