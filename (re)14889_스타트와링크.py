'''
1. 능력치 구하기
2. 조합
'''
from itertools import combinations

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
total = {i for i in range(n)}

ans = 1e9
for c1 in combinations({i for i in range(n)},n//2):
    c1 = set(c1)
    c2 = total - set(c1)
    tmp1 = 0
    tmp2 = 0
    for x in range(n):
        for y in range(x):
            if x in c1 and y in c1:
                tmp1 += board[x][y] + board[y][x]
            elif x in c2 and y in c2:
                tmp2 += board[x][y] + board[y][x]
    if abs(tmp2-tmp1) < ans:
        ans = abs(tmp2-tmp1)

print(ans)