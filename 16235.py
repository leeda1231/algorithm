n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
a = [[5]*n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)

# 봄
for i in range(n):
    for j in range(n):
        if tree[i][j]:
            for age in len(1,tree[i][j]+1):
                pass