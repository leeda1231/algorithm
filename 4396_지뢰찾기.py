n = int(input())
bomb = [list(input()) for _ in range(n)]
games = [list(input()) for _ in range(n)]
dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,1,-1]
ans = [[0]*n for _ in range(n)]

def play():
    global ans
    flag = 0
    for i in range(n):
        for j in range(n):
            if games[i][j] == 'x' and bomb[i][j] == '*':
                flag = 1
            if games[i][j] == '.':
                ans[i][j] = '.'

    for x in range(n):
        for y in range(n):
            if flag == 1 and bomb[x][y] == '*':
                ans[x][y] = '*'
            cnt = 0
            if ans[x][y] == 0:
                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and bomb[nx][ny] == '*':
                        cnt += 1
                ans[x][y] += cnt

    return

play()
for a in ans:
    print(''.join(list(map(str,a))))