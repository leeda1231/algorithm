def pal1(i,j,n):
    s = j
    e = j+n-1
    if j > 8-n:
        return 0
    while s < e:
        if arr[i][s] != arr[i][e]:
            return 0
        s += 1
        e -= 1
    return 1

def pal2(i,j,n):
    s = i
    e = i+n-1
    if i > 8-n:
        return 0
    while s < e:
        if arr[s][j] != arr[e][j]:
            return 0
        s += 1
        e -= 1
    return 1


for tc in range(10):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    ans = 0
    for i in range(8):
        for j in range(8):
            ans += pal1(i,j,n) + pal2(i,j,n)
    print(f'#{tc+1} {ans}')