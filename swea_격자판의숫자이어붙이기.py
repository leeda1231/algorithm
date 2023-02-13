dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y,s,n):
    global nums
    if n == 7:
        nums.add(s)
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx,ny,s+arr[nx][ny],n+1)



T = int(input())
for tc in range(T):
    arr = [list(input().split()) for _ in range(4)]
    nums = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j],1)
    print(f'#{tc+1}',len(nums))