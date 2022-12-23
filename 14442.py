from collections import deque 

n,m,k = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
v = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
q = deque([(0,0)])
while q:
    x,y,z = q.popleft()
    if x == n-1 and y == m-1:
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and v[nx][ny][z] == 0:
                
else:
    print(-1)