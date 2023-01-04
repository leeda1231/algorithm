from collections import deque
n,q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**n)]
lst = list(map(int,input().split()))
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for l in lst:
    # 회전
    tmp = [[0]*(2**n) for _ in range(2**n)]
    for x in range(0,2**n,2**l):
        for y in range(0,2**n,2**l):
            for i in range(2**l):
                for j in range(2**l):
                    tmp[x+j][y+(2**l-1)-i] = arr[x+i][y+j]
    # 얼음 녹이기
    # 근접한 얼음의 개수가 3개 미만이면 녹인다.
    lst_melt = []
    for i in range(2**n):
        for j in range(2**n):
            if tmp[i][j] != 0:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<2**n and 0<=ny<2**n and tmp[nx][ny] != 0:
                        cnt += 1
                if cnt < 3:
                    lst_melt.append((i,j))
    for i,j in lst_melt:
        tmp[i][j] -= 1   
    
    arr = tmp

# 얼음의 합
total = 0
for i in range(2**n):
    for j in range(2**n):
        total += arr[i][j]
print(total)

# 덩어리 bfs
def bfs(i,j):
    global cnt
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        cnt += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<2**n and 0<=ny<2**n and arr[nx][ny] != 0 and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx,ny))


cnt_max = 0
v = [[0]*(2**n) for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        cnt = 0
        if arr[i][j] != 0 and v[i][j] == 0:
            v[i][j] = 1
            total += arr[i][j]
            bfs(i,j)
        if cnt_max < cnt:
            cnt_max = cnt
print(cnt_max)