from collections import deque

def bfs(i,j):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = deque()
    q.append((i,j))
    v = [[0]*n for _ in range(n)]
    v[i][j] = 1
    ans = arr[i][j]
    while q:
        x,y = q.popleft()
        if v[x][y] < n//2+1:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                    ans += arr[nx][ny]
                    v[nx][ny] = v[x][y] + 1
                    q.append((nx,ny))
    return ans


T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    i,j = n//2,n//2
    print(f'#{tc+1} {bfs(i,j)}')