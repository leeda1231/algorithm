from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))
    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == m-1:
            return v[x][y][z]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                # 벽을 안 부시고 가는 경우
                if v[nx][ny][z] == 0 and arr[nx][ny] == 0:
                    v[nx][ny][z] = v[x][y][z] + 1
                    q.append((nx,ny,z))
                # 벽을 부시고 가는 경우
                elif z == 0 and arr[nx][ny] == 1: # 벽을 아직 부수지 않은거면 벽 부순 방문처리 당연히 안 한 것.
                    v[nx][ny][1] = v[x][y][z] + 1
                    q.append((nx,ny,1))
    
    return -1


v = [[[0]*2 for _ in range(m)] for _ in range(n)]
v[0][0][0] = 1
print(bfs(0,0,0))

