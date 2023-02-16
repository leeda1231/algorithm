n = int(input())
cnt = 0
arr = [[0]*101 for _ in range(101)]
for _ in range(n):
    r,c = map(int,input().split())
    for x in range(r,r+10):
        for y in range(c,c+10):
            if arr[x][y] == 0:
                arr[x][y] = 1
                cnt += 1
print(cnt)