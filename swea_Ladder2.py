# 좌 우 상
dx = [0,0,-1]
dy = [-1,1,0]

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    min_v = 10000
    ans = 0
    for j in range(100):
        if arr[99][j] == 1:
            v = [[0] * 100 for _ in range(100)]
            x,y = 99,j
            v[x][y] = 1
            tmp = 1
            while x > 0:
                for d in range(3):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1 and v[nx][ny] == 0:
                        tmp += 1
                        x,y = nx,ny
                        v[x][y] = 1
                        break
            if tmp < min_v:
                min_v = tmp
                ans = y
    print(f'#{tc} {ans}')