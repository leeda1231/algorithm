#1
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def restore():
    q = deque()
    q.append((0,0))
    inf = int(1e9)
    v = [[inf]*n for _ in range(n)]
    v[0][0] = 0
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] > v[x][y] + arr[nx][ny]:
                v[nx][ny] = v[x][y] + arr[nx][ny]
                q.append((nx,ny))
    return v[-1][-1]



T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    ans = restore()
    print(f'#{tc+1} {ans}')