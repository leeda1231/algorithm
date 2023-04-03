from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    arr[x][y] = '.'
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<h and 0<=ny<w and arr[nx][ny] == '#':
                q.append((nx,ny))
                arr[nx][ny] = '.'

T = int(input())

for tc in range(T):
    h, w = map(int,input().split())
    arr = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#':
                bfs(i,j)
                cnt += 1

    print(cnt)