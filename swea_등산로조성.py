dx = [0,1,0,-1]
dy = [1,0,-1,0]

def high():
    max_v = 0
    h = []
    for i in range(n):
        max_v = max(max_v,max(arr[i]))
    for x in range(n):
        for y in range(n):
            if arr[x][y] == max_v:
                h.append((x,y))
    return h

def dfs(x,y,flag,cnt):
    global ans
    ans = max(ans,cnt)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
            if flag == 1:
                if arr[nx][ny] < arr[x][y]:
                    v[nx][ny] = 1
                    dfs(nx,ny,flag,cnt+1)
                    v[nx][ny] = 0
            else:
                if arr[nx][ny] < arr[x][y]:
                    v[nx][ny] = 1
                    dfs(nx, ny, flag, cnt + 1)
                    v[nx][ny] = 0
                elif arr[nx][ny] - (arr[x][y] - 1) <= k:
                    v[nx][ny] = arr[nx][ny]
                    arr[nx][ny] = arr[x][y] - 1
                    dfs(nx,ny,flag+1,cnt+1)
                    arr[nx][ny] = v[nx][ny]
                    v[nx][ny] = 0


T = int(input())
for tc in range(T):
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    h = high()
    ans = 0
    for i,j in h:
        v = [[0]*n for _ in range(n)]
        v[i][j] = 1
        dfs(i,j,0,1)
    print(f'#{tc+1} {ans}')