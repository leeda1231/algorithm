dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int,input().split())
x,y,d = map(int,input().split())
# (r,c)는 0부터 시작한다 => 문제 잘 읽기
x += 1
y += 1
area = [[1]*(n+2)] + [([1] + list(map(int,input().split())) + [1]) for _ in range(n)] + [[1]*(n+2)]
area[x][y] = 2
answer = 1

while 1:
    for _ in range(4):
        d = (d-1) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        #1
        if area[nx][ny] == 0:
            x = nx
            y = ny
            area[x][y] = 2
            answer += 1
            break
    else:    
        if area[x-dx[d]][y-dy[d]] == 1:
            break
        x -= dx[d]
        y -= dy[d]

print(answer)