# 1
from collections import deque
 
def bfs(x,y):
    q = deque()
    q.append((x,y))
    s = []
    s.append(arr[x][y])
    v[x][y] = 1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and abs(arr[nx][ny] - arr[x][y]) == 1 and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = 1
                s.append(arr[nx][ny])
    return min(s),len(s)  
 
T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    cnt = 0
    num = n*n
    v = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                st,l = bfs(i,j)
                if l > cnt or (l == cnt and st < num):
                    cnt = l
                    num = st
    print(f'#{tc+1}',num,cnt)


# 2
from collections import deque

def bfs(x,y):
    global tmp
    q = deque()
    q.append((x,y))
    v[x][y] = 1
    tmp = 1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] + 1 and v[nx][ny] == 0:
                q.append((nx,ny))
                v[nx][ny] = v[x][y] + 1
                tmp = v[nx][ny]

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    cnt = 0
    s = arr[0][0]
    for i in range(n):
        for j in range(n):
            v = [[0]*n for _ in range(n)]
            bfs(i,j)
            if tmp > cnt:
                cnt = tmp
                s = arr[i][j]
            elif tmp == cnt and s > arr[i][j]:
                s = arr[i][j]
    print(f'#{tc+1}',s,cnt)
