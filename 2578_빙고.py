board = [list(map(int,input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int,input().split()))

# 정답: i+1
def bingo():
    for idx in range(25):
        for i in range(5):
            for j in range(5):
                if board[i][j] == mc[idx]:
                    board[i][j] = 0
        if check(board) == 'bingo':
            return idx+1

def check(arr):
    cnt = 0
    # 가로
    for i in range(5):
        if sum(arr[i]) == 0:
            cnt += 1
    
    # 세로    
    for j in range(5):
        total = 0
        for i in range(5):
            total += arr[i][j]
        if total == 0:
            cnt += 1
    
    # 대각선
    total_1 = 0
    total_2 = 0
    for i in range(5):
        total_1 += arr[i][i]
        total_2 += arr[i][4-i]
    if total_1 == 0:
        cnt += 1
    if total_2 == 0:
        cnt += 1
    
    if cnt >= 3:
        return 'bingo'    
    return

print(bingo())