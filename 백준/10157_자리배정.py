C, R = map(int,input().split())
K = int(input())
# 편의를 위해 오른쪽으로 90도 회전하여 생각
# C | R ㅡ
# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 달팽이, 인덱스 주의(나중에 +1)
arr = [[0]*R for _ in range(C)]
x = y = d = 0
for i in range(1,C*R+1):
    arr[x][y] = i
    x = x + dx[d]
    y = y + dy[d]

    if 0 <= x < C and 0 <= y < R and arr[x][y] == 0:
        continue
    else:
        x -= dx[d]
        y -= dy[d]
        d = (d+1) % 4
        x += dx[d]
        y += dy[d]

ans = 0
for i in range(C):
    for j in range(R):
        if arr[i][j] == K:
            ans = i+1,j+1
            break

if ans == 0:
    print(ans)
else:
    print(*ans)