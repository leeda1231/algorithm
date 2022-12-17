from collections import deque
a,b,c = map(int,input().split())
total = a+b+c
v = [[0] * 1501 for _ in range(1501)]

def bfs(a,b,c):
    q = deque([(a,b,c)])
    v[a][b] = 1
    while q:
        x,y,z = q.popleft()
        if x == y and y == z:
            return 1
        if x < y:
            if v[x*2][y-x] == 0:
                v[x*2][y-x] = 1
                q.append((x*2,y-x,z))
        if y < x:
            if v[x-y][y*2] == 0:
                v[x-y][y*2] = 1
                q.append((x-y,y*2,z))
        if x < z:
            if v[x*2][y] == 0:
                v[x*2][y] = 1
                q.append((x*2,y,z-x))
        if z < x:
            if v[x-z][y] == 0:
                v[x-z][y] = 1
                q.append((x-z,y,z*2))
        if y < z:
            if v[x][y*2] == 0:
                v[x][y*2] = 1
                q.append((x,y*2,z-y))
        if z < y:
            if v[x][y-z] == 0:
                v[x][y-z] = 1
                q.append((x,y-z,z*2))
    return 0
    
if total % 3 == 0:
    print(bfs(a,b,c))
else:
    print(0)