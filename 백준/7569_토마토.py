from collections import deque

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while q:
        x,y,z = q.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and arr[nz][nx][ny] == 0 and v[nz][nx][ny] == 0:
                q.append((nx,ny,nz))
                arr[nz][nx][ny] = arr[z][x][y] + 1
                v[nz][nx][ny] = 1


m,n,h = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
v = [[[0]*m for _ in range(n)] for _ in range(h)]
ans = 0
q = deque()

for k in range(h):
    for i in range(n):  
        for j in range(m):
            if arr[k][i][j] == 1:
                q.append((i,j,k))

bfs()

max_v = 0
for k in range(h):
    for i in range(n):  
        for j in range(m):
            if arr[k][i][j] == 0:
                ans = -1
            max_v = max(max_v,arr[k][i][j])

if ans == -1:
    print(-1)
else:
    print(max_v-1)