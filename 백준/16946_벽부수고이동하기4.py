from collections import deque
n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
group = {0:0, 1:0}

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    global cnt
    q = deque([(x,y)])
    v[x][y] = 1
    board[x][y] = idx
    while q:
        x,y = q.popleft()
        cnt += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and v[nx][ny] == 0:
                v[nx][ny] = 1
                board[nx][ny] = idx
                q.append((nx,ny))

idx = 2
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and v[i][j] == 0:
            cnt = 0
            bfs(i,j)
            group[idx] = cnt
            idx += 1

new_board = [[0]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            new_board[x][y] = 1
            tmp = set()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    tmp.add(board[nx][ny])
            for t in tmp:
                new_board[x][y] += group[t]
            new_board[x][y] %= 10

for n in new_board:
    print(''.join(map(str,n)))