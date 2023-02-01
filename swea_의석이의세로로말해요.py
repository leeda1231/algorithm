T = int(input())
for tc in range(T):
    arr = []
    max_length = 0
    ans = ''
    for _ in range(5):
        lst = list(input())
        n = len(lst)
        if n > max_length:
            max_length = n
        arr.append(lst)
    for i in range(5):
        if len(arr[i]) < max_length:
            arr[i] += [''] * (max_length-len(arr[i]))
    for j in range(max_length):
        for i in range(5):
            ans += arr[i][j]

    print(f'#{tc+1}',ans)