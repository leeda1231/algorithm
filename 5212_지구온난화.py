r,c = map(int,input().split())
arr = [list(input()) for _ in range(r)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
lst = []

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'X':
            cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<r and 0<=ny<c and arr[nx][ny] == 'X':
                    continue
                cnt += 1
            if cnt >= 3:
                lst.append((i,j))


for x,y in lst:
    arr[x][y] = '.'


min_r = r
min_c = c
max_r = -1
max_c = -1
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'X':
            if min_r > i:
                min_r = i
            if max_r < i:
                max_r = i
            if min_c > j:
                min_c = j
            if max_c < j:
                max_c = j

for i in range(min_r,max_r+1):
    for j in range(min_c,max_c+1):
        print(arr[i][j],end='')
    print()
                    