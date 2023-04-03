r,c,n = map(int,input().split())
grid = [list(input()) for _ in range(r)]
grid_even = [['O']*c for _ in range(r)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for time in range(1,n+1):
    if time == 1:
        continue
    if time % 2 == 0:
        grid_tmp = [['O']*c for _ in range(r)]
        continue
    # 폭탄 터트리는 로직
    else:
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'O':
                    grid_tmp[x][y] = '.'
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < r and 0 <= ny < c:
                            grid_tmp[nx][ny] = '.'
    grid = grid_tmp

if n % 2 == 0:
    for answer in grid_even:
        print(''.join(answer))
else:
    for answer in grid:
        print(''.join(answer))
