for tc in range(10):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for j in range(n):
        flag = 0
        for i in range(n):
            if arr[i][j] == 1:
                flag = 1
            elif arr[i][j] == 2 and flag == 1:
                ans += 1
                flag = 0
    print(f'#{tc+1} {ans}')