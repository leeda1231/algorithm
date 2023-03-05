# 좌 우 상
dx = [0,0,-1]
dy = [-1,1,0]

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    v = [[0]*100 for _ in range(100)]
    finish = arr[99].index(2)
    x,y = 99,finish
    v[x][y] = 1
    while x > 0:
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1 and v[nx][ny] == 0:
                x,y = nx,ny
                v[x][y] = 1
                break
    print(f'#{tc} {y}')