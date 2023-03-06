from collections import deque

def bfs(i,j):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    v[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0 and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx,ny))
    return x,y

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    v = [[0]*n for _ in range(n)]
    lst = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and v[i][j] == 0:
                cnt += 1
                ii,jj = bfs(i,j)
                lst.append([ii-i+1,jj-j+1])
    lst.sort(key=lambda x:(x[0]*x[1],x[0]))
    print(f'#{tc+1} {cnt}',end=' ')
    for l in lst:
        print(*l,end=' ')
    print()