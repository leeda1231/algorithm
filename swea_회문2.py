def pal(arr,n):
    for i in range(100):
        for j in range(100):
            if j+n < 100:
                s = j
                e = j+n
                while s <= e:
                    if arr[i][s] != arr[i][e]:
                        break
                    s += 1
                    e -= 1
                else:
                    return n+1
                s = j
                e = j + n
                while s <= e:
                    if arr[s][i] != arr[e][i]:
                        break
                    s += 1
                    e -= 1
                else:
                    return n+1
    return 0


for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    n = 99
    ans = 1
    while n > 1:
        x = pal(arr,n)
        if x > ans:
            ans = x
            break
        n -= 1
    print(f'#{tc} {ans}')