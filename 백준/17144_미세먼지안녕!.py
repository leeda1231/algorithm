from pprint import pprint

r,c,T = map(int,input().split())
room = []
for i in range(r):
    room.append(list(map(int,input().split())))
    if room[i][0] == -1:
        fresh_d = i
fresh_u = fresh_d - 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 확산
def spread():
    v = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if (x,y) != (fresh_u,0) and (x,y) != (fresh_d,0):
                cnt = 0
                arr = []
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and (nx,ny) != (fresh_u,0) and (nx,ny) != (fresh_d,0):
                        cnt += 1
                        arr.append((nx,ny))
                if cnt > 0:
                    for i,j in arr:
                        v[i][j] += room[x][y] // 5
                    v[x][y] -= (room[x][y] // 5) * cnt
    
    for x in range(r):
        for y in range(c):
            room[x][y] += v[x][y]

dx_u = [0,-1,0,1]
dy_u = [1,0,-1,0]
# 공기청정기 작동
def move1():
    x,y = fresh_u,1
    d = 0
    last = room[x][y]
    room[x][y] = 0
    while 1:
        nx = x + dx_u[d]
        ny = y + dy_u[d]
        if (nx,ny) == (fresh_u,0):
            return
        if 0 <= nx < r and 0 <= ny < c:
            next = room[nx][ny]
            room[nx][ny] = last
            last = next
            x,y = nx,ny
        else:
            d += 1

dx_d = [0,1,0,-1]
dy_d = [1,0,-1,0]
def move2():
    x,y = fresh_d,1
    d = 0
    last = room[x][y]
    room[x][y] = 0
    while 1:
        nx = x + dx_d[d]
        ny = y + dy_d[d]
        if (nx,ny) == (fresh_d,0):
            return
        if 0 <= nx < r and 0 <= ny < c:
            next = room[nx][ny]
            room[nx][ny] = last
            last = next
            x,y = nx,ny
        else:
            d += 1

for _ in range(T):
    spread()
    move1()
    move2()

ans = 2
for i in room:
    ans += sum(i)
print(ans)


'''
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