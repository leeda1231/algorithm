T = int(input())
for tc in range(T):
    ans = 0
    n,m = map(int,input().split())
    arr = [[0] + list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(1,n+1):
            arr[i][j] += arr[i][j-1]

    for i in range(n-m+1):
        for j in range(m,n+1):
            fly = 0
            for k in range(m):
                fly += arr[i+k][j] - arr[i+k][j-m]
            if fly > ans:
                ans = fly
    print(f'#{tc+1}',ans)