n, l, r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    tmp = arr[i][j]
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 < nx or nx > n or 0 < ny or ny > n:
                continue
            if l <= arr[nx][ny] <= r:
                q.append((nx,ny))
                tmp += arr[nx][ny]
    