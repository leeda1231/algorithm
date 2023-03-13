def check(x,y,d):
    while 1:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 1:
                return 0
            x,y = nx,ny
            continue
        else:
            return 1

def change(x,y,d):
    l = 0
    while 1:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            arr[nx][ny] = arr[nx][ny] ^ 1
            x,y = nx,ny
            l += 1
        else:
            return l



def dfs(cnt,length,idx):
    global max_core, min_length, m
    # 가지치기
    if cnt + m - idx < max_core:
        return
    if cnt > max_core:
        max_core = cnt
        min_length = length
    elif cnt == max_core and 0 < length < min_length:
        min_length = length
    if idx < m:
        i = cores[idx][0]
        j = cores[idx][1]
        for d in range(4):
            if check(i,j,d):
                l = change(i,j,d)
                dfs(cnt+1,length+l,idx+1)
                change(i,j,d)
        dfs(cnt,length,idx+1)



T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    cores = []
    m = 0
    max_core = 0
    min_length = 200
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] == 1:
                cores.append((i,j))
                m += 1
    dfs(0,0,0)
    if min_length == 200:
        min_length = 0
    print(f'#{tc+1} {min_length}')