direction = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)}
move_dir = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
bombs = [0,0,0,0]
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
magics = [list(map(int,input().split())) for _ in range(m)]

def magic(d,s):
    x = n//2
    y = n//2
    for dis in range(1,s+1):
        nx = x + direction[d][0] * dis
        ny = y + direction[d][1] * dis
        board[nx][ny] = 0
    return

def move():
    global oneline
    d = 0
    num = 1
    x = n//2
    y = n//2
    oneline = []
    while 1:
        for _ in range(2):
            for _ in range(num):
                nx = x + move_dir[d][0]
                ny = y + move_dir[d][1]
                if board[nx][ny] != 0:
                    oneline.append(board[nx][ny])
                if (nx,ny) == (0,0):
                    return oneline
                x = nx
                y = ny
            d = (d+1) % 4
        num += 1
    return

def bomb():
    global oneline
    newline = []
    flag = 0
    cnt = 1
    tmp = -1
    for i in range(len(oneline)):
        if oneline[i] != tmp:
            tmp = oneline[i]
            if cnt >= 4:
                for _ in range(cnt):
                    x = newline.pop()
                bombs[x] += cnt
                flag = 1
            cnt = 0
        newline.append(oneline[i])
        cnt += 1
    if cnt >= 4:
        for _ in range(cnt):
            x = newline.pop()
        bombs[x] += cnt
        flag = 1
    oneline = newline[:]
    return flag

def change():
    global board
    newline = [0]
    tmp = oneline[0]
    cnt = 1
    for i in range(1,len(oneline)):
        if oneline[i] != tmp:
            newline.append(cnt)
            newline.append(tmp)
            tmp = oneline[i]
            cnt = 0
        cnt += 1
    newline.append(cnt)
    newline.append(oneline[-1])
    
    if len(newline) < n*n:
        for _ in range(n*n - len(newline)):
            newline.append(0)
    d = 0
    num = 1
    x = n//2
    y = n//2
    idx = 1
    while 1:
        for _ in range(2):
            for _ in range(num):
                nx = x + move_dir[d][0]
                ny = y + move_dir[d][1]
                board[nx][ny] = newline[idx]
                idx += 1
                if (nx,ny) == (0,0):
                    return
                x = nx
                y = ny
            d = (d+1) % 4
        num += 1


for d,s in magics:
    magic(d,s)
    move()
    again = 1
    while again:
        again = bomb()
    if len(oneline) == 0:
        break
    change()

answer = bombs[1] + 2*bombs[2] + 3*bombs[3]
print(answer)