def rotate(arr):
    arr = [list(reversed(list(r))) for r in zip(*arr)]
    return arr


T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)
    print(f'#{tc+1}')
    for i in range(n):
        print(''.join(map(str,arr1[i])),''.join(map(str,arr2[i])),''.join(map(str,arr3[i])))