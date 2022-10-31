dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int,input().split())
x,y,d = map(int,input().split())
area = [[1]*(n+2)] + [([1] + list(map(int,input().split())) + [1]) for _ in range(n)] + [[1]*(n+2)]
area[x][y] = 2
answer = 1

while 1:
    d = (d-1) % 4
    nx = x + dx[d]
    ny = y + dy[d]
    rotate_cnt = 1
    #1
    if area[nx][ny] == 0:
        x = nx
        y = ny
        area[x][y] = 2
        answer += 1
        continue
    #3,4
    if rotate_cnt > 3 and area[nx][ny] == 1:
        break
    elif rotate_cnt > 3 and area[nx][ny] != 1:
        x = nx
        y = ny 
        continue
    #2
    else:
        rotate_cnt += 1

print(answer)