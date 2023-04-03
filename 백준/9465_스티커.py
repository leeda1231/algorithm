T = int(input())

def dp(n, board):
    if n == 1:
        return max(board[0][0], board[1][0])
    if n == 2:
        return max(board[0][0]+board[1][1], board[1][0]+board[0][1])
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    dp[0][1] = board[1][0] + board[0][1]
    dp[1][1] = board[0][0]+board[1][1]
    for i in range(2,n):
        dp[0][i] = max(dp[0][i-2],dp[1][i-2],dp[1][i-1]) + board[0][i]
        dp[1][i] = max(dp[0][i-2],dp[1][i-2],dp[0][i-1]) + board[1][i]
    return max(dp[0][n-1],dp[1][n-1])
        

for _ in range(T):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(2)]
    print(dp(n,board))