from collections import deque
# 우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n = int(input())
picture = [list(input()) for _ in range(n)]
visited_1 = [[0]*n for _ in range(n)]
visited_2 = [[0]*n for _ in range(n)]

def bfs_1(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited_1[nx][ny] == 0 and picture[x][y] == picture[nx][ny]:
                q.append((nx,ny))
                visited_1[nx][ny] = 1

def bfs_2(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited_2[nx][ny] == 0:
                if ((picture[x][y] == 'R' or picture[x][y] == 'G') and (picture[nx][ny] == 'R' or picture[nx][ny] == 'G')) or (picture[x][y] == 'B' and picture[nx][ny] == 'B'):
                    q.append((nx,ny))
                    visited_2[nx][ny] = 1

bfs_1(0,0)
bfs_2(0,0)
visited_1[0][0] = 1
visited_2[0][0] = 1
cnt_1 = 1
cnt_2 = 1
for i in range(n):
    for j in range(n):
        if visited_1[i][j] == 0:
            bfs_1(i,j)
            cnt_1 += 1
        if visited_2[i][j] == 0:
            bfs_2(i,j)
            cnt_2 += 1

print(cnt_1,cnt_2)