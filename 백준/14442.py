from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
board = [list(input()) for _ in range(n)]
v = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    q = deque([(0,0,0)])
    v[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == m-1:
           return v[n-1][m-1][z]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny][z] == 0:
                if board[nx][ny] == '0':
                    v[nx][ny][z] = v[x][y][z] + 1
                    q.append((nx,ny,z))
                elif board[nx][ny] == '1' and z < k:
                    v[nx][ny][z+1] = v[x][y][z] + 1
                    q.append((nx,ny,z+1))
    return -1

print(bfs())