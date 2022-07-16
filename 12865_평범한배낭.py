n,k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
# 가방에 넣을 수 있는 물건을 하나씩 돌려준다 (누적)
for i in range(1,n+1):
    w,v = map(int,input().split())
    # 가방의 무게 1~K까지 정하기
    for j in range(1,k+1):
        # 내 물건을 가방에 넣을 수 있다면
        if w <= j:
            # dp[i-1][j] : 내 물건을 안 넣는 경우
            # dp[i-1][j-w] + v : 내 물건을 넣는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        # 내 물건의 무게가 가방의 최대 무게보다 크다면 못 들어감.
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])