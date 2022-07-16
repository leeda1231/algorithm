from collections import deque
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 우하좌상 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    dis = []
    visited = [[0]*n for _ in range(n)]
    visited[a][b] = 1
    
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                    if arr[nx][ny] == 1:
                        dic[(a,b)] += abs(a-nx)+abs(b-ny)
    
    return dis

dic = {}
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            dic[(i,j)] = 0
            

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            bfs(i,j)

print(dic)
