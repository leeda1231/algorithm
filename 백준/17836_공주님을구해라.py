from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m and (arr[nx][ny] == 0 or arr[nx][ny] == -2):
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))

n,m,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
# 검을 -2로 바꾸기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            arr[i][j] = -2
            a,b = i,j # 검의 인덱스 저장

bfs(0,0)

# 검을 얻지 않고 가는 경우
t1 = arr[n-1][m-1] # t1이 0이라면 못간 것

# 검을 얻어서 가는 경우
t2 = 0
if arr[a][b] != -2:
    t2 = arr[a][b] + (n-1-a) + (m-1-b)

# 검도 못 얻고 도착도 못한 경우 둘다 0
if t1==0 and t2==0:
    print('Fail')

elif t1==0 and t2!=0:
    if t2 <= t:
        print(t2)
    else:
        print('Fail')

elif t1!=0 and t2==0:
    if t1 <= t:
        print(t1)
    else:
        print('Fail')

elif t1!=0 and t2!=0:
    ans = min(t1,t2)
    if ans <= t:
        print(ans)
    else:
        print('Fail')
