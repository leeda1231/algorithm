from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j] = house
    cnt = 1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = house
                cnt += 1
    return cnt

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
v = [[0]*n for _ in range(n)]
house = 0
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == 0:
            house += 1
            ans.append(bfs(i,j))

ans.sort()
print(house)
for i in ans:
    print(i)