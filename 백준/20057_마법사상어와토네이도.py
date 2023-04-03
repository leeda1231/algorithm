'''
이동하는 인덱스
그에 따른 모래 이동
바깥에 나오는 모래 찾기
'''
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
sand = 0
# 왼 아래 오 위
dx = [0,1,0,-1]
dy = [-1,0,1,0]


def tornado(x,y,d):
    global sand
    center = board[x][y]
    total = 0
    percent = [7,7,2,2,1,1,10,10,5]
    dir = [(0,1), (0,-1), (0,2), (0,-2), (1,1), (1,-1), (-1,1), (-1,-1), (-2,0),(-1,0)]   
    x_idx = (d%2 + 1) % 2
    y_idx = d%2
    if d == 1 or d == 2:
        sign = -1
    elif d == 3 or d == 0:
        sign = 1
    for i in range(9):
        nx = x + (sign) * dir[i][x_idx]
        ny = y + (sign) * dir[i][y_idx]
        val = (center * percent[i]) // 100
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] += val
        else:
            sand += val
        total += val
    nx = x + (sign) * dir[9][x_idx]
    ny = y + (sign) * dir[9][y_idx]
    if 0 <= nx < n and 0 <= ny < n:
        board[nx][ny] += center - total
    else:
        sand += center - total
    board[x][y] = 0

def snail():
    cnt = 0
    s = 1 # 거리
    d = 0 # 방향
    x,y = n//2, n//2 # 시작점
    while 1:
        for _ in range(2):
            for _ in range(s):
                if cnt == n*n-1:
                    return
                cnt += 1
                nx = x + dx[d]
                ny = y + dy[d]
                if board[nx][ny] != 0:
                    tornado(nx,ny,d)
                x,y = nx,ny
            d = (d+1) % 4
        s += 1

snail()
print(sand)