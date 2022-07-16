N, K = map(int,input().split())
w = [0,0,0,0,0,0]
m = [0,0,0,0,0,0]
cnt = 0
for i in range(N):
    S, Y = map(int,input().split())
    if S == 0:
        w[Y-1] += 1
    else:
        m[Y-1] += 1


for i in w + m:
    if i % K == 0:
        cnt += i // K
    else:
        cnt += i // K + 1

print(cnt)