n = int(input())
time = []
price = []
for _ in range(n):
    t,p = map(int,input().split())
    time.append(t)
    price.append(p)

dp = [0] * (n+1)
for i in range(n-1,-1,-1):
    if i + time[i] > n:
        dp[i] = dp[i+1]
        continue
    dp[i] = max(dp[i+1], price[i] + dp[i+time[i]])

print(dp[0])

# n = int(input())
# t = []
# p = []
# for _ in range(n):
#     a,b = map(int,input().split())
#     t.append(a)
#     p.append(b)

# dp = [0] * (n+1) # 맨 끝에꺼 0으로 놔주기 위해, 인덱스는 한칸씩 밀림.

# for i in range(n-1,-1,-1):
#     if i + t[i] > n:
#         dp[i] = dp[i+1]
#     else:
#         # dp[i+1]은 현재일자를 선택 안하는 경우
#         # 현재일자를 선택하는 경우
#         dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])

# print(dp[0])
