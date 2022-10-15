a = [(1,0),(0,1)]
v = [[0]*2 for _ in range(2)]
for x,y in a:
    v[x][y] = 1
print(v)
