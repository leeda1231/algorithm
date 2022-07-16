from pprint import pprint
r,c,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(r)]
# 우 상 좌 하
dx = [0,-1,0,1]
dy = [1,0,-1,0]

for i in range(r):
    if arr[i][0] == -1:
        fresh = i
        break
down = fresh + 1  
  
for _ in range(T):
    tmp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                lst = []
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        cnt += 1
                        lst.append((nx,ny))
                tmp[i][j] -= (arr[i][j] // 5) * cnt
                for nx, ny in lst:
                    tmp[nx][ny] += arr[i][j] // 5

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp[i][j]

    # 확산
    # 위쪽
    d = 0
    x,y = fresh, 1
    val = arr[x][y]
    arr[x][y] = 0
    while 1:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == fresh and ny == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue
        if 0<= nx <r and 0<=ny<c:
            arr[nx][ny], val = val, arr[nx][ny]
            x,y = nx, ny

    # 아래
    # 우 하 좌 상
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d = 0
    x,y = down, 1
    val = arr[x][y]
    arr[x][y] = 0
    while 1:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == down and ny == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue
        if 0<= nx <r and 0<=ny<c:
            arr[nx][ny], val = val, arr[nx][ny]
            x,y = nx, ny

total = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != -1:
            total += arr[i][j]

pprint(arr)


'''
틀렸습니다
    확산 위쪽
    v
    for i in range(fresh-1,0,-1):
        if i == fresh-1:
            arr[i][0] = 0
        else:
            arr[i][0] = arr[i-1][0]

    # <
    for j in range(0,c-1):
        arr[0][j] = arr[0][j+1]

    # ^
    for i in range(1,fresh+1):
        arr[i-1][-1] = arr[i][-1]

    # >
    for j in range(c-2,0,-1):
        arr[fresh][j+1] = arr[fresh][j]

    arr[fresh][1] = 0

    # 확산 아래쪽
    # fresh + 1
    # ^ < v >
    # ^
    for i in range(down+1,r-1):
        arr[i][0] = arr[i+1][0]

    # <
    for j in range(c-1):
        arr[r-1][j] = arr[r-1][j+1]

    # v
    for i in range(r-1,down,-1):
        arr[i][c-1] = arr[i-1][c-1]

    # >
    for j in range(c-1,1,-1):
        arr[down][j] = arr[down][j-1]

    arr[down][1] = 0

total = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != -1:
            total += arr[i][j]

print(total)
print(arr)
'''