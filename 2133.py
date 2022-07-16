dp = [0]*31
dp[2] = 3
for i in range(4,31,2):
    # 다 차 있을 때
    dp[i] = dp[i-2] * 3
    # 홀수칸
    

n = int(input())
print(dp[n])