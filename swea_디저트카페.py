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

