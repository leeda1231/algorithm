import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[100000001]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1],c)


for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == 100000001:
            arr[i][j] = 0

for ans in arr:
    print(*ans)