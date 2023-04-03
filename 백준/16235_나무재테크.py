import sys

input = sys.stdin.readline

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,1,-1]

n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
land = [[5 for _ in range(n)] for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)

for _ in range(k):
    # 봄
    for i in range(n):
        for j in range(n):
            if not tree[i][j]:
                continue
            new_tree = []
            food = 0
            while tree[i][j]:
                x = tree[i][j].pop()
                # 양분 부족
                if x > land[i][j]:
                    # 여름
                    food += x // 2
                else:
                    new_tree.append(x+1)
                    land[i][j] -= x
            tree[i][j] = new_tree[::-1]
            land[i][j] += food

    # 가을, 겨울
    for x in range(n):
        for y in range(n):
            land[x][y] += arr[x][y]
            if not tree[x][y]:
                continue
            for t in tree[x][y]:
                if t % 5 == 0:
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].append(1)

answer = 0
for x in range(n):
    for y in range(n):
        answer += len(tree[x][y])

print(answer)