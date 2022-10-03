n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

num_minus = 0
num_zero = 0
num_plus = 0

def dfs(x,y,n):
    global num_minus, num_zero, num_plus
    tmp = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j] != tmp:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*(n//3),y+l*(n//3),n//3)
                return
    if tmp == -1:
        num_minus += 1
    elif tmp == 0:
        num_zero += 1
    else:
        num_plus += 1

dfs(0,0,n)
print(num_minus)
print(num_zero)
print(num_plus)