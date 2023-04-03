from collections import deque

n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j
        
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ans = -1

def move(x,y,dx,dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x,y,cnt

def bfs(rx,ry,bx,by,count):
    global ans
    q = deque([(rx,ry,bx,by,count)])
    v = []
    v.append((rx,ry,bx,by))
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt > 10:
            return
        for d in range(4):
            tmp_rx,tmp_ry,r_cnt = move(rx,ry,dx[d],dy[d])
            tmp_bx,tmp_by,b_cnt = move(bx,by,dx[d],dy[d])
            if board[tmp_bx][tmp_by] == 'O':
                continue
            if board[tmp_rx][tmp_ry] == 'O':
                ans = cnt
                return
            if tmp_rx == tmp_bx and tmp_ry == tmp_by:
                if r_cnt > b_cnt:
                    tmp_rx -= dx[d]
                    tmp_ry -= dy[d]
                else:
                    tmp_bx -= dx[d]
                    tmp_by -= dy[d]
            if (tmp_rx,tmp_ry,tmp_bx,tmp_by) not in v:
                v.append((tmp_rx,tmp_ry,tmp_bx,tmp_by))
                q.append((tmp_rx,tmp_ry,tmp_bx,tmp_by,cnt+1))
    return

bfs(rx,ry,bx,by,1)
print(ans)