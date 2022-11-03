from itertools import combinations
from collections import deque
n,m,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def attack(y):
    q = deque([(n,y,1)])
    v = [[0]*m for _ in range(n)]
    while q:
        x,y,dis = q.popleft()
        if dis > d:
            return (-1,-1)
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0:
                if board[nx][ny] == 1:
                    return (nx,ny)
                v[nx][ny] = 1
                q.append((nx,ny,dis+1))


for j1,j2,j3 in combinations([i for i in range(m)],3):
    Archer1 = (n+1,j1)
    Archer2 = (n+1,j2)
    Archer3 = (n+1,j3)
    x1,y1 = attack(j1)
    x2,y2 = attack(j2)
    x3,y3 = attack(j3)
    s = set()
    if x1 != -1:
        s.add((x1,y1))
    if x2 != -1:
        s.add((x2,y2))
    if x3 != -1:
        s.add((x3,y3))