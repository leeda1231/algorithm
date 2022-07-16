n,k = map(int,input().split())
coins = []
dp = [0] * (k+1)
for _ in range(n):
    coin = int(input())
    # 동전이 100,000보다 작거나 같고 k <= 10000 이라서
    if coin <= k:
        coins.append(coin)

for i in range(1,k+1):
    for coin in coins:
        for j in range(i):
            if i == j + coin:
                dp[i] += 1

print(dp)