n,m = map(int,input().split())
baskets = [list(map(int,input().split())) for _ in range(n)]
moves = [list(map(int,input().split())) for _ in range(m)]
clouds = [[0]*n for _ in range(n)]
clouds[n-1][0] = 1
clouds[n-1][1] = 1
clouds[n-2][0] = 1
clouds[n-2][1] = 1
direction = {1:(0,-1), 2: (-1,-1), 3:(-1,0), 4:(-1,1), 5:(0,1), 6:(1,1), 7:(1,0), 8:(1,-1)}
answer = 0

def move(d,s):
    global move_set
    move_set = set()
    for x in range(n):
        for y in range(n):
            if clouds[x][y] == 1:
                nx = (x + s * direction[d][0]) % n
                ny = (y + s * direction[d][1]) % n
                move_set.add((nx,ny))
                clouds[x][y] = 0
    for x,y in move_set:
        clouds[x][y] = 1
    return
        
def water_copy(x,y):
    cnt = 0
    for d in range(2,9,2):
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if 0 <= nx < n and 0 <= ny < n:
            if baskets[nx][ny] > 0:
                cnt += 1
    baskets[x][y] += cnt
    return


for d,s in moves:
    move(d,s)
    for x,y in move_set:
        baskets[x][y] += 1
        clouds[x][y] = 0
    for x,y in move_set:
        water_copy(x,y)
    for x in range(n):
        for y in range(n):
            if baskets[x][y] > 1 and (x,y) not in move_set:
                baskets[x][y] -= 2
                clouds[x][y] = 1

for x in range(n):
    for y in range(n):
        answer += baskets[x][y]
print(answer)

'''
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dis = {1:(0,-1),2:(-1,-1),3:(-1,0),4:(-1,1),5:(0,1),6:(1,1),7:(1,0),8:(1,-1)}
v = [[0]*n for _ in range(n)]

v[n-1][0] = 1
v[n-1][1] = 1
v[n-2][0] = 1
v[n-2][1] = 1

for _ in range(m):
    d,s = map(int,input().split())
    # 1
    goaway = []
    for i in range(n):
        for j in range(n):
            if v[i][j] == 1:
                v[i][j] = 0
                nx = (i + dis[d][0]*s) % n
                ny = (j + dis[d][1]*s) % n
                # v[nx][ny] = 1
                goaway.append((nx,ny))
                # 2
                arr[nx][ny] += 1
                # 3
                # v[nx][ny] = 0
    
    # 4
    goaway_add = []
    for x,y in goaway:
        cnt = 0
        for dx,dy in ((-1,-1),(-1,1),(1,1),(1,-1)):
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] > 0:
                cnt += 1
        goaway_add.append((x,y,cnt))
    
    for x,y,cnt in goaway_add:
        arr[x][y] += cnt

    # 5
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i,j) not in goaway:
                v[i][j] = 1
                arr[i][j] -= 2

ans = 0
for i in arr:
    ans += sum(i)

print(ans)
'''
        



                