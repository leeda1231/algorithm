#2 bfs
from collections import deque

def bfs(i,j,n,m):
    global ans
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = deque()
    v = [[0] * n for _ in range(n)]
    cnt_lst = [0] * (n+1)
    if arr[i][j] == 1:
        cnt_lst[1] = 1
    q.append((i, j, 1))
    v[i][j] = 1
    while q:
        x,y,cnt = q.popleft()
        if cnt < n:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    if arr[nx][ny] == 1:
                        cnt_lst[cnt+1] += 1
                    q.append((nx,ny,cnt+1))
    val = cnt_lst[1]
    for idx in range(2,n+1):
        val += cnt_lst[idx]
        if m*val - cost_lst[idx] >= 0:
            ans = max(ans,val)


T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 1
    max_cnt = 0
    for i in range(n):
        max_cnt += arr[i].count(1)
    c = (n+1)*(n+1) + n*n
    p = m*max_cnt
    if p - c >= 0:
        ans = max_cnt
    else:
        cost_lst = [k*k + (k-1)*(k-1) for k in range(n+1)]
        for i in range(n):
            for j in range(n):
                bfs(i,j,n,m)

    print(f'#{tc+1} {ans}')


#1 구현
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