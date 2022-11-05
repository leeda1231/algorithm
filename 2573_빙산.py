from collections import deque

n,m = map(int,input().split())
north = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def oneYear():
    v = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if north[x][y] != 0:
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if north[nx][ny] == 0:
                            cnt += 1
                v[x][y] = cnt
    total = 0
    for x in range(n):
        for y in range(m):
            north[x][y] -= v[x][y]
            if north[x][y] < 0:
                north[x][y] = 0
            total += north[x][y]
    return total

def check():
    global visited
    answer = 0
    while 1:
        total = oneYear()
        if total == 0:
            return 0
        answer += 1
        visited = [[0]*m for _ in range(n)]
        cnt = 0
        for x in range(n):
            for y in range(m):
                if north[x][y] != 0 and visited[x][y] == 0:
                    bfs(x,y)
                    cnt += 1
                    
        if cnt > 1:
            return answer

def bfs(x,y):
    global visited
    q = deque([(x,y)])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and north[nx][ny] != 0 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
    return

print(check())