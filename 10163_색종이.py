N = int(input())
arr = [[0]*1001 for _ in range(1001)]
for n in range(1,N+1):
    x, y, w, h = map(int,input().split())
    for i in range(x,x+w):
        arr[i][y:y+h] = [n] * h

for n in range(1,N+1):
    cnt = 0
    for i in arr:
        cnt += i.count(n)
    print(cnt)