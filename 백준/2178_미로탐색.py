from collections import deque
n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] != 0 and v[nx][ny] == 0:
                    maze[nx][ny] += maze[x][y]
                    v[nx][ny] = 1
                    q.append((nx,ny))


bfs()
print(maze[-1][-1])