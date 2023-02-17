#1
def dia(d,i,j):
    cnt = 0
    for dx in range(-d+1,d):
        ddx = abs(dx)
        for dy in range(ddx-d+1,d-ddx):
            nx = i + dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                cnt += 1
    return cnt

def cctv(d):
    global m, ans, max_v
    cost = d*d + (d-1)*(d-1)
    for i in range(n):
        for j in range(n):
            cnt = dia(d,i,j)
            if cnt*m - cost >= 0 and cnt > ans:
                ans = cnt
            if ans == max_v:
                return

T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_v = 0 # 가지치기
    for a in arr:
        max_v += a.count(1)
    # k == 1
    ans = 1
    if n%2:
        k = n
    else:
        k = n+1

    for d in range(2,k+1):
        cctv(d)

    print(f'#{tc+1}',ans)