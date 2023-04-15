from collections import deque

def bfs(x,y,v,maps,n,m):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = deque()
    q.append((x,y))
    v[x][y] = 1
    cnt = int(maps[x][y])
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and maps[nx][ny] != 'X':
                q.append((nx,ny))
                v[nx][ny] = 1
                cnt += int(maps[nx][ny])
    return cnt
        
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    v = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if v[i][j] == 0 and maps[i][j] != 'X':
                answer.append(bfs(i,j,v,maps,n,m))
    answer.sort()
    if answer == []:
        answer = [-1]
    return answer