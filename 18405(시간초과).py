# 시간초과
from collections import deque

n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
s,ans_x,ans_y = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(T):
    q = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == T:
                q.append((i,j))
    
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = T
    T += 1
    if T <= s:
        bfs(T)

cnt = 0

while cnt < s:
    for i in range(1,k+1):
        bfs(i)
        cnt += 1
    

print(arr[ans_x-1][ans_y-1])
