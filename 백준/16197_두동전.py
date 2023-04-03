import sys
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
coins = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coins.append([i,j])

x1,y1,x2,y2 = coins[0][0],coins[0][1],coins[1][0],coins[1][1]
cnt = 0
min_val = 11

def dfs(x1,y1,x2,y2,cnt):
    global min_val
    if cnt >= 10:
        min_val = min(min_val,11)
        return
    
    for d in range(4):
        nx1 = x1 + dx[d]
        ny1 = y1 + dy[d]
        nx2 = x2 + dx[d]
        ny2 = y2 + dy[d]
        # 둘 다 안
        if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < m and 0 <= ny2 < m:
            # nx1,ny1 벽
            if board[nx1][ny1] == '#':
                nx1 = x1
                ny1 = y1
            # nx2,ny2 벽
            if board[nx2][ny2] == '#':
                nx2 = x2
                ny2 = y2
            dfs(nx1,ny1,nx2,ny2,cnt+1)
        # nx2,ny2만 떨어짐
        elif 0 <= nx1 < n and 0 <= ny1 < m:
            min_val = min(min_val,cnt+1)
            return
        # nx1,ny1만 떨어짐
        elif 0 <= nx2 < n and 0 <= ny2 < m:
            min_val = min(min_val,cnt+1)
            return
        # 둘 다 떨어짐
        else:
            continue

dfs(x1,y1,x2,y2,cnt)
if min_val == 11:
    min_val = -1
print(min_val)