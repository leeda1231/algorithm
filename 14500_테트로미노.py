import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y,num,total):
    global ans

    if ans > total + max_v * (4-num): # 최대값 가지치기
        return
    
    if num == 4:
        ans = max(ans,total)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<=nx<n and 0<=ny<m and v[nx][ny] == 0:
            v[nx][ny] = 1
            if num == 2:
                dfs(x,y,num+1,total+arr[nx][ny])    
            dfs(nx,ny,num+1,total+arr[nx][ny])
            v[nx][ny] = 0

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
ans = 0
max_v = max(map(max,arr))

for i in range(n):
    for j in range(m):
        v[i][j] = 1
        dfs(i,j,1,arr[i][j])
        v[i][j] = 0

print(ans)