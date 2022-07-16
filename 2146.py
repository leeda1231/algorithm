from collections import deque
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

# 다른섬임을 구별할 수 있는 country 배열 만들기
country = [[0]*n for _ in range(n)]
v = [[0]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs1(x,y):
    global val
    q = deque()
    q.append((x,y))
    v[0][0] = 1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx,ny))
                country[nx][ny] += val
                v[nx][ny] = 1

val = 1
country[0][0] = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == 0:
            bfs1(i,j)
            val += 1

# bfs 돌려서 가장 짧은 다리 찾기
def bfs2(num):
    global ans
    q = deque()
    # 바다랑 다른 섬은 -1, 이번 섬은 0
    dis = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if country[i][j] == num:
                q.append((i,j))
                dis[i][j] = 0
    
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if country[nx][ny] == 0  and dis[nx][ny] == -1:
                    dis[nx][ny] = dis[x][y] + 1
                    q.append((nx,ny))
                if country[nx][ny] != 0 and country[nx][ny] != num:
                    ans = min(ans, dis[x][y])
                    
                    return

ans = 10000
for i in range(1,val):
    bfs2(i)

print(ans)



# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 0:
#             arr[i][j] = 200


# def bfs(x,y):
#     global visited
#     q = deque()
#     q.append((x,y))
#     visited =[[0]*n for _ in range(n)]
#     visited[0][0] = 1
#     while q:
#         x,y = q.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and visited[nx][ny] == 0:
#                 q.append((nx,ny))
#                 arr[nx][ny] = min(arr[nx][ny], arr[x][y] + 1)
#                 visited[nx][ny] = 1

# visited =[[0]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1 and visited[i][j] == 0:
#             bfs(i,j)
# pprint(arr)


# bfs 돌려서 가장 짧은 다리 찾기
# def bfs2(x,y):
#     q = deque()
#     q.append((x,y))
#     visited[0][0] = 1
#     while q:
#         x,y = q.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if 0 <= nx < n and 0 <= ny < n and country[nx][ny] != country[x][y]:
#                 q.append((nx,ny))
#                 country[nx][ny] += val
#                 v[nx][ny] = 1

# visited = [[0]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if country[i][j] != 0:
#             pass
