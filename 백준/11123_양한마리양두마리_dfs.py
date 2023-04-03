# 재귀 깊이 제한 늘려주는 것
import sys
sys.setrecursionlimit(3000000)

T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(i,j):
    arr[i][j] = '.'
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0<=nx<h and 0<=ny<w and arr[nx][ny] == '#':
            dfs(nx,ny)
    

for tc in range(T):
    h, w = map(int,input().split())
    arr = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#':
                dfs(i,j)
                cnt += 1

    print(cnt)
