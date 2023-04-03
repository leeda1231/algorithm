n = int(input())
garden = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

garden_cost = [[0]*(n-2) for _ in range(n-2)]
for x in range(1,n-1):
    for y in range(1,n-1):
        garden_cost[x-1][y-1] += garden[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            garden_cost[x-1][y-1] += garden[nx][ny]

visited = [[0] * (n-2) for _ in range(n-2)]
ans = 1e9
tmp = 0
def dfs(cnt):
    global ans, tmp
    if cnt == 3:
        ans = min(ans, tmp)
        return
    for i in range(n-2):
        for j in range(n-2):
            if visited[i][j] == 0:
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < n-2 and 0 <= nj < n-2 and visited[ni][nj] == 1:
                        break
                else:
                    tmp += garden_cost[i][j]
                    visited[i][j] = 1
                    for d in range(4):
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if 0 <= ni < n-2 and 0 <= nj < n-2 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                    dfs(cnt+1)
                    tmp -= garden_cost[i][j]
                    visited[i][j] = 0
                    for d in range(4):
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if 0 <= ni < n-2 and 0 <= nj < n-2:
                            visited[ni][nj] = 0

dfs(0)
print(ans)