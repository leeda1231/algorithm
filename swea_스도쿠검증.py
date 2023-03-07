def validation(arr):
    # 가로 세로
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            row.add(arr[i][j])
            col.add(arr[j][i])
        if len(row) < 9 or len(col) < 9:
            return 0
    # 네모
    for i in range(1,8,3):
        for j in range(1,8,3):
            s = set()
            for dx,dy in [(0,0),(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                s.add(arr[i+dx][j+dy])
            if len(s) < 9:
                return 0
    return 1


T = int(input())
for tc in range(T):
    arr = [list(map(int,input().split())) for _ in range(9)]
    print(f'#{tc+1} {validation(arr)}')