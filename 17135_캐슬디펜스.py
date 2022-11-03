from copy import deepcopy
from itertools import combinations
from collections import deque
n,m,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx = [0,-1,0]
dy = [-1,0,1]

def attack(y):
    q = deque([(n,y,1)])
    v = [[0]*m for _ in range(n)]
    while q:
        x,y,dis = q.popleft()
        if dis > d:
            return (-1,-1)
        for dir in range(3):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0:
                if tmp_board[nx][ny] == 1:
                    return (nx,ny)
                v[nx][ny] = 1
                q.append((nx,ny,dis+1))


def move():
    last = tmp_board[0]
    for i in range(1,n):
        new = tmp_board[i]
        tmp_board[i] = last
        last = new
    tmp_board[0] = [0]*m
    return


max_val = 0
for j1,j2,j3 in combinations([i for i in range(m)],3):
    total = 0
    tmp_board = deepcopy(board)
    while 1:
        # attack
        x1,y1 = attack(j1)
        x2,y2 = attack(j2)
        x3,y3 = attack(j3)
        s = set()
        if x1 != -1:
            s.add((x1,y1))
            tmp_board[x1][y1] = 0
        if x2 != -1:
            s.add((x2,y2))
            tmp_board[x2][y2] = 0
        if x3 != -1:
            s.add((x3,y3))
            tmp_board[x3][y3] = 0
        total += len(s)

        # check
        check = 0
        for i in range(n):
            check += sum(tmp_board[i])
        if check == 0:
            break
        # move
        move()
    # answer
    if max_val < total:
        max_val = total

print(max_val)