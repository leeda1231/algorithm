board = [[1,2],[3,4]]
n = 2
m = 2
last = board[0]
for i in range(1,n):
    new = board[i]
    print(last)
    board[i] = last
    print(board[i])
    last = new
board[0] = [0]*m
print(board)