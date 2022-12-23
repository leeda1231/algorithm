# 벽을 뚫지 않았을 때 더 빨리 도착할 경우, 나중에 있는 벽은 그때 먼저 뚫린다?
from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
v = [[[0,0] for _ in range(m)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque([(0,0,0)])
while q:
    x,y,z = q.popleft()
    if x == n-1 and y == m-1:
        print(v[x][y][z]+1)
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if v[nx][ny][z] == 0 and board[nx][ny] == 0:
                v[nx][ny][z] = v[x][y][z] + 1
                q.append((nx,ny,z))
            elif z == 0 and board[nx][ny] == 1:
                v[nx][ny][1] = v[x][y][z] + 1
                q.append((nx,ny,1))
else:
    print(-1)



'''
# 이전 풀이
from pprint import pprint
from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))
    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == m-1:
            return v[x][y][z]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                # 벽을 안 부시고 가는 경우
                if v[nx][ny][z] == 0 and arr[nx][ny] == 0:
                    v[nx][ny][z] = v[x][y][z] + 1
                    q.append((nx,ny,z))
                # 벽을 부시고 가는 경우
                elif z == 0 and arr[nx][ny] == 1: # 벽을 아직 부수지 않은거면 벽 부순 방문처리 당연히 안 한 것.
                    v[nx][ny][1] = v[x][y][z] + 1
                    q.append((nx,ny,1))
    
    return -1


v = [[[0]*2 for _ in range(m)] for _ in range(n)]
v[0][0][0] = 1
print(bfs(0,0,0))

# 시간초과
from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
lst = [(0,0)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            lst.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and new_board[nx][ny] == 0:
                v[nx][ny] = 1
                new_board[nx][ny] = new_board[x][y] + 1
                q.append((nx,ny))


    
min_val = 1000000
for r,c in lst:
    new_board = [b[:] for b in board]
    new_board[r][c] = 0
    v = [[0] * m for _ in range(n)]
    bfs(0,0)
    if new_board[-1][-1] != 0:
        if new_board[-1][-1] < min_val:
            min_val = new_board[-1][-1]

if min_val == 1000000:
    print(-1)
else:
    print(min_val+1)
'''