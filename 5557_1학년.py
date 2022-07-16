from pprint import pprint

n = int(input())
numbers = list(map(int,input().split()))
# 0이상 20이하(중간계산값)
dp = [[0]*21 for _ in range(n)]
dp[0][numbers[0]] = 1

for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]:
            if 0<= j + numbers[i] < 21:
                dp[i][j + numbers[i]] += dp[i-1][j]
            if 0<= j - numbers[i] < 21:
                dp[i][j - numbers[i]] += dp[i-1][j]

print(dp[n-2][numbers[-1]])