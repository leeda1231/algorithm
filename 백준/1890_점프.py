# dp

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] >= 1 and arr[i][j] != 0:
            dx = i + arr[i][j]
            dy = j + arr[i][j]
            if dx < n:
                dp[dx][j] += dp[i][j]
            if dy < n:
                dp[i][dy] += dp[i][j]

print(dp[-1][-1])
