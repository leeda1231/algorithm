from collections import deque

# 우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny))


# N: 행, M: 열
M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0

# 모든 토마토가 익어있는 상태
cnt = 0
for i in arr:
    cnt += sum(i)
    if cnt == N*M:
        print(0)
        break
# 아니면
else:
    bfs()
    for i in arr:
        if 0 in i:
            print(-1)
            break
        ans = max(ans,max(i))
    else:
        print(ans-1)
        

