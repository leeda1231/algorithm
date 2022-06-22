from collections import deque, defaultdict

n = int(input())
k = int(input())
apple = set()
for _ in range(k):
    x,y = map(int,input().split())
    apple.add((x-1,y-1))
l = int(input())
change_dir = defaultdict(str)
for _ in range(l):
    a,b = input().split()
    change_dir[int(a)] = b

snake = deque([(0,0)])
time = 0
# 우 하 좌 상 (방향 L일땐 -1)
dx = [0,1,0,-1]
dy =[1,0,-1,0]
d = 0
while snake:
    time += 1
    x,y = snake.popleft()
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx,ny) in snake:
        break
    if (nx,ny) in apple:
        apple.remove((nx,ny))
        snake.appendleft((x,y))
    else:
        snake.appendleft((x,y))
        snake.pop()
    snake.appendleft((nx,ny))
    if change_dir[time]:
        if change_dir[time] == 'D':
            d = (d+1) % 4
        else:
            d = (d-1) % 4

print(time)