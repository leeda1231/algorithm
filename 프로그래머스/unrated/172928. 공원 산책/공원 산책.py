def solution(park, routes):
    direction = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    r,c = len(park),len(park[0])
    for i in range(len(park)):
        if 'S' in park[i]:
            x,y = i,park[i].index('S')
            break
    for route in routes:
        d,s = route.split()
        s = int(s)
        nx = x + direction[d][0]*s
        ny = y + direction[d][1]*s
        if 0 <= nx < r and 0 <= ny < c:
            if nx == x:
                if y < ny:
                    for j in range(y+1,ny+1):
                        if park[nx][j] == 'X':
                            break
                    else:
                        x,y = nx,ny
                else:
                    for j in range(ny,y):
                        if park[nx][j] == 'X':
                            break
                    else:
                        x,y = nx,ny
            if ny == y:
                if x < nx:
                    for i in range(x+1,nx+1):
                        if park[i][ny] == 'X':
                            break
                    else:
                        x,y = nx,ny
                else:
                    for i in range(nx,x):
                        if park[i][ny] == 'X':
                            break
                    else:
                        x,y = nx,ny       
    answer = [x,y]
    return answer