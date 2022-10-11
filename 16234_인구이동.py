from collections import deque
n,l,r = map(int,input().split())
land = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ans = 0

def bfs(x,y):
    global flag
    q = deque([(x,y)])
    v[x][y] = 1
    arr = []
    total = 0
    while q:
        x,y = q.popleft()
        arr.append((x,y))
        total += land[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                if l <= abs(land[nx][ny] - land[x][y]) <= r:
                    q.append((nx,ny))
                    v[nx][ny] = 1
    if len(arr) == 1:
        return
    flag = 1
    for i,j in arr:
        land[i][j] = total // len(arr)
    return
    

while 1:
    flag = 0
    v = [[0]*n for _ in range(n)]
    # bfs 반복
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                bfs(i,j)
    # 종료조건 => bfs 한번도 안돌때까지
    if flag == 0:
        break
    ans += 1

print(ans)

'''
n, l, r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    tmp = arr[i][j]
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 < nx or nx > n or 0 < ny or ny > n:
                continue
            if l <= arr[nx][ny] <= r:
                q.append((nx,ny))
                tmp += arr[nx][ny]
'''