'''
0: 빈 칸 1: 벽 2: 바이러스
1. 벽을 세운다.
2. 바이러스를 퍼뜨린다.
3. 안전 영역의 크기를 구한다.
'''

from itertools import combinations
from collections import deque
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

# 벽을 세울 리스트
lst = []
cnt1 = 3
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            lst.append((i,j))
        elif board[i][j] == 1:
            cnt1 += 1

# 바이러스 퍼뜨리기
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    global cnt2
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        cnt2 += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and new_board[nx][ny] == 0:
                v[nx][ny] = 1
                new_board[nx][ny] = 2
                q.append((nx,ny))

max_val = 0
for w1,w2,w3 in combinations(lst,3):
    new_board = [b[:] for b in board]
    new_board[w1[0]][w1[1]] = 1
    new_board[w2[0]][w2[1]] = 1
    new_board[w3[0]][w3[1]] = 1
    v = [[0]*m for _ in range(n)]
    cnt2 = 0
    for x in range(n):
        for y in range(m):
            if new_board[x][y] == 2 and v[x][y] == 0:
                bfs(x,y)
    safe_area = n*m - cnt1 - cnt2
    if safe_area > max_val:
        max_val = safe_area

print(max_val)



'''
# 이전 풀이
from itertools import combinations
from collections import deque
from copy import deepcopy

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 0에서 1이라는 벽 세 개 세우기 위함.
lst = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            lst.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and arr_tmp[nx][ny] == 0:
                queue.append((nx,ny))
                arr_tmp[nx][ny] = 2

ans = 0
for idx in list(combinations(lst,3)):
    arr_tmp = deepcopy(arr)
    for a in idx:
        arr_tmp[a[0]][a[1]] = 1
    
    lst_2 = []
    for i in range(n):
        for  j in range(m):
            if arr_tmp[i][j] == 2:
                lst_2.append((i,j))
    
    for i in lst_2:
        bfs(i[0],i[1])
    
    cnt = 0
    for i in arr_tmp:
        cnt += i.count(0)

    ans = max(ans,cnt)

print(ans)
'''