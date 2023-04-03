n = int(input())
# lst = [int(input()) for _ in range(n)]
lst = []
for _ in range(n):
    x = int(input())
    lst.append(x)

# LIS, Longest Increasing Subsequence Problem
# 가장 긴 증가하는 부분수열에 포함되는 아이들 빼고 움직이기
dp = [0] * n
dp[0] = 1
# dp[i]를 구하는 과정
for i in range(1,n):
    tmp = []
    for j in range(i):
        if lst[i] > lst[j]:
            tmp.append(dp[j])
        if not tmp:
            dp[i] = 1
        # if not tmp에 대한 else
        else:
            dp[i] = max(tmp) + 1

print(n-max(dp))