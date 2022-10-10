from collections import deque
T = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    v[x][y] = 0
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if v[nx][ny] > v[x][y] + roads[nx][ny]:
                    v[nx][ny] = v[x][y] + roads[nx][ny]
                    q.append((nx,ny))
    return            

for tc in range(T):
    n = int(input())
    roads = [list(map(int,input())) for _ in range(n)]
    v = [[1e16]*n for _ in range(n)]
    bfs(0,0)
    print(f'#{tc+1} {v[-1][-1]}')