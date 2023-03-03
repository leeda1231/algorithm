for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    max_v = sum(arr[0])
    for i in range(100):
        max_v = max(max_v,sum(arr[i]))
    d_left = 0
    d_right = 0
    for j in range(100):
        column = 0
        for i in range(100):
            column += arr[i][j]
            if i == j:
                d_right += arr[i][j]
            if i + j == 99:
                d_left += arr[i][j]
        max_v = max(max_v,column)
    max_v = max(max_v,d_left,d_right)
    print(f'#{tc} {max_v}')