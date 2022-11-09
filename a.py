from pprint import pprint

n = 3
board = [[[] for _ in range(n)] for _ in range(n)]
board[1][1].append([1,2,3])
board[1][1].append([2,3,4])
pprint(board)