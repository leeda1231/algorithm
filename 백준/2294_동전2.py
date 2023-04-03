n,k = map(int,input().split())
coins = []
dp = [10001] * (k+1)
dp[0] = 0
for _ in range(n):
    coin = int(input())
    # 동전이 100,000보다 작거나 같고 k <= 10000 이라서
    if coin <= k:
        coins.append(coin)

for i in range(1,k+1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])