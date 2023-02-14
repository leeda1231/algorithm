#2
T = int(input())
dir = {0:(1,1),1:(1,-1),2:(-1,-1),3:(-1,1)}

def dfs(x,y,d,cnt):
    global ans
    if d == 3 and x == sx and y == sy:
        if ans < cnt:
            ans = cnt
        return
    for dd in range(d,d+2):
        if dd != 4:
            nx = x + dir[dd][0]
            ny = y + dir[dd][1]
            if 0 <= nx < n and 0 <= ny < n and dessert[arr[nx][ny]] == 0:
                dessert[arr[nx][ny]] = 1
                dfs(nx,ny,dd,cnt+1)
                dessert[arr[nx][ny]] = 0

for tc in range(T):
    ans = -1
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n-1):
        for j in range(1,n-1):
            dessert = [0] * 101
            sx,sy = i,j
            dfs(i,j,0,0)
    print(f'#{tc+1}',ans)


#1
T = int(input())

dx = [1,1,-1,-1,0]
dy = [-1,1,1,-1,0]

def dfs(n,x,y):
    global ans, cnt, sx, sy, v
    if n > 3:
        return
    if n == 3 and sx == x and sy == y and ans < cnt:
        ans = cnt
        return
    for d in range(n,n+2):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and v[cafe[nx][ny]] == 0:
            v[cafe[nx][ny]] = 1
            cnt += 1
            dfs(d,nx,ny)
            v[cafe[nx][ny]] = 0
            cnt -= 1

for tc in range(T):
    N = int(input())
    cafe = [list(map(int,input().split())) for _ in range(N)]
    ans = -1
    for sx in range(0,N-2):
        for sy in range(1,N-1):
            v = [0] * 101
            cnt = 0
            dfs(0,sx,sy)

    print(f'#{tc+1} {ans}')

