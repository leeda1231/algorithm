n,m = map(int,input().split())

office = []
cctv = []
for i in range(n):
    data = list(map(int,input().split()))
    office.append(data)
    for j in range(m):
        if 0 < data[j] < 6:
            cctv.append((i,j))
            
mode = dict()
mode[1] = [[0],[1],[2],[3]]
mode[2] = [[0,2],[1,3]]
mode[3] = [[0,1],[1,2],[2,3]]
mode[4] = [[0,1,2],[0,1,3],[0,2,3],[1,2,3]]
mode[5] = [[0,1,2,3]]

