from collections import deque

T = int(input())
u,d,l,r = (-1,0),(1,0),(0,-1),(0,1)
tunnel = {1:[u,d,l,r],2:[u,d],3:[l,r],4:[u,r],5:[d,r],6:[d,l],7:[u,l]}

def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    v[x][y] = 1
    while q:
        x,y = q.popleft()
        if v[x][y] == l:
            return cnt
        for dx,dy in tunnel[arr[x][y]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and arr[nx][ny] != 0:
                for ddx,ddy in tunnel[arr[nx][ny]]:
                    if dx*ddx + dy*ddy == -1:
                        q.append((nx,ny))
                        v[nx][ny] = v[x][y] + 1
                        cnt += 1
                        break
    return cnt


for tc in range(T):
    n,m,r,c,l = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    v = [[0]*m for _ in range(n)]
    ans = bfs(r,c)
    print(f'#{tc+1}',ans)


# 아마도 교수님 풀이
from collections import deque

T = int(input())
u,d,l,r = (-1,0),(1,0),(0,-1),(0,1)
tunnel = {1:[u,d,l,r],2:[u,d],3:[l,r],4:[u,r],5:[d,r],6:[d,l],7:[u,l]}

def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    v[x][y] = 1
    while q:
        x,y = q.popleft()
        if v[x][y] == l:
            return cnt
        for dx,dy in tunnel[arr[x][y]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and arr[nx][ny] != 0:
                for ddx,ddy in tunnel[arr[nx][ny]]:
                    if dx*ddx + dy*ddy == -1:
                        q.append((nx,ny))
                        v[nx][ny] = v[x][y] + 1
                        cnt += 1
                        break
    return cnt


for tc in range(T):
    n,m,r,c,l = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    v = [[0]*m for _ in range(n)]
    ans = bfs(r,c)
    print(f'#{tc+1}',ans)