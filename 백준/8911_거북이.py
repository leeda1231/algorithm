T = int(input())
# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(T):
    lst = list(input())
    x,y = 0,0
    d = 0
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    #1 방향바꾸기, 앞 뒤 이동
    for l in lst:
        if l == 'R':
            d = (d+1) % 4
        elif l == 'L':
            d = (d-1) % 4
        
        elif l == 'F':
            nx = x + dx[d]
            ny = y + dy[d]
            # 가장작은 x,y and 가장큰 x,y(지나간 영역 포함하는 가장 작은 직사각형 넓이 구하기)
            if nx > max_x:
                max_x = nx
            elif nx < min_x:
                min_x = nx
            if ny > max_y:
                max_y = ny
            elif ny < min_y:
                min_y = ny
            x,y = nx,ny

        elif l == 'B':
            nx = x - dx[d]
            ny = y - dy[d]
            if nx > max_x:
                max_x = nx
            elif nx < min_x:
                min_x = nx
            if ny > max_y:
                max_y = ny
            elif ny < min_y:
                min_y = ny
            x,y = nx,ny

    ans = (max_x-min_x) * (max_y-min_y)
    
    print(ans)