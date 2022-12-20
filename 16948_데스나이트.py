from collections import deque

n = int(input())
r1,c1,r2,c2 = map(int,input().split())
board = [[0]*n for _ in range(n)]
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
v = [[0]*n for _ in range(n)]
v[r1][c1] = 1
q = deque([(r1,c1)])
board[r2][c2] = -1

while q:
    x,y = q.popleft()
    if x == r2 and y == c2:
        break
    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            v[nx][ny] = 1
            q.append((nx,ny))

print(board[r2][c2])