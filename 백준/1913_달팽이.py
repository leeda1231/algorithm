# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
m = int(input())
snail = [[0]*n for _ in range(n)]

x,y = n//2, n//2
d = 0
snail[x][y] = 1
if m == 1:
    xx,yy = n//2+1, n//2+1

# 방향을 언제 바꾸는지
for i in range(1,n+1):
    for _ in range(2):
        for j in range(i):
            nx = x + dx[d]
            ny = y + dy[d]
            snail[nx][ny] = snail[x][y] + 1
            if snail[nx][ny] == m:
                xx,yy = nx+1, ny+1
            x,y = nx, ny
        if i == n:
            break
        d = (d+1) % 4
snail[n-1][0] -= n
for s in snail:
    print(*s)
print(xx,yy)