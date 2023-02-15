dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,1,-1]

def play(x,y,s,d,cnt,lst):
    global tmp, tmp_list
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        if board[nx][ny] == s:
            tmp_list = lst
            tmp = cnt
            return
        elif board[nx][ny] == 2//s:
            play(nx,ny,s,d,cnt+1,lst+[(nx,ny)])

T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    board = [[0]*n for _ in range(n)]
    board[n//2-1][n//2-1] = 2
    board[n//2][n//2] = 2
    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1
    stone = [0,2,2]
    for _ in range(m):
        x,y,s = map(int,input().split())
        stone[s] += 1
        board[x-1][y-1] = s
        # you = 2//s
        for d in range(8):
            tmp = 0
            tmp_list = []
            play(x-1, y-1, s, d, 0,[])
            for i,j in tmp_list:
                board[i][j] = s
            stone[s] += tmp
            stone[2//s] -= tmp
    print(f'#{tc+1} {stone[1]} {stone[2]}')