from pprint import pprint

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
total = 0

for i in range(n):
    for j in range(1,n):
        arr[i][j] += arr[i][j-1]
        if j == n-1:
            total += arr[i][n-1]

# 1
d1 = 0
x = 0
y = 0
one = 0
idx = 0
for i in range(x+d1):
    one += arr[i-idx][y] 
    if i >= x:
        idx += 1

# 2
