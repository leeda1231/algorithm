n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
magic = [list(map(int,input().split())) for _ in range(m)]
direction = {1: (-1,0), 2: (1,0), 3: (0,-1), 4: (0,1)}
dx = [0,1,0,-1]
dy = [-1,0,1,0]
ans = [0,0,0,0]


def destroy(d,s):
    x,y = n//2, n//2
    for dis in range(1,s+1):
        nx = x + dis * direction[d][0]
        ny = y + dis * direction[d][1]
        board[nx][ny] = 0
    return


def move():
    x,y = n//2, n//2
    lst = []
    s = 1
    d = 0
    while 1:
        for _ in range(2):
            for _ in range(s):
                nx = x + dx[d]
                ny = y + dy[d]
                if board[nx][ny] != 0:
                    lst.append(board[nx][ny])
                if nx == 0 and ny == 0:
                    return lst
                x,y = nx,ny
            d = (d+1) % 4
        s += 1



def bomb(lst):
    flag = 0
    last = -1
    cnt = 1
    new_lst = []
    for i in range(len(lst)):
        if last != lst[i]:
            last = lst[i]
            new_lst.append(lst[i])
            cnt = 1
            continue
        cnt += 1
        new_lst.append(lst[i])
        if cnt == 4:
            flag = 1
            ans[last] += 4
            for _ in range(4):
                new_lst.pop()
        elif cnt > 4:
            ans[last] += 1
            new_lst.pop()
    return flag, new_lst


def change():
    lst.append(0)
    last = lst[0]
    cnt = 1
    new_lst = []
    num = 1
    for i in range(1,len(lst)):
        if num > n*n:
            break
        if last != lst[i]:
            new_lst.append(cnt)
            new_lst.append(last)
            last = lst[i]
            cnt = 1
            num += 2
            continue
        cnt += 1
    if num < n*n:
        new_lst += [0] * (n*n-num)

    x,y = n//2, n//2
    s = 1
    d = 0
    idx = 0
    board[x][y] = 0
    while 1:
        for _ in range(2):
            for _ in range(s):
                nx = x + dx[d]
                ny = y + dy[d]
                board[nx][ny] = new_lst[idx]
                if nx == 0 and ny == 0:
                    return
                idx += 1
                x,y = nx,ny
            d = (d+1) % 4
        s += 1


for i in range(m):
    d,s = magic[i]
    destroy(d,s)
    lst = move()
    flag = 1
    while flag:
        flag, lst = bomb(lst)
    change()

print(ans[1] + 2*ans[2] + 3*ans[3])

'''
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
'''