
def chess(arr,x,y):
    v = 0
    tmp = arr[x][y]
    for i in range(x,x+8):
        for j in range(y,y+8):
            if arr[i][j] != tmp:
                v += 1
            if tmp == 'W':
                tmp = 'B'
            else:
                tmp = 'W'
        if tmp == 'W':
                tmp = 'B'
        else:
            tmp = 'W'
    return min(v,64-v)


def play(n,m):
    ans = 64
    for x in range(n-7):
        for y in range(m-7):
            val = chess(arr,x,y)
            if ans > val:
                ans = val
            if ans == 0:
                return ans
    return ans


n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
print(play(n,m))