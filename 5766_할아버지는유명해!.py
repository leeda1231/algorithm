while 1:
    v = [[0,i] for i in range(10001)]
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    for _ in range(n):
        lst = map(int,input().split())
        for l in lst:
            v[l][0] += 1
    v.sort(reverse=True)
    max_val = v[1][0]
    answer = []
    for i in range(1,10001):
        if max_val != v[i][0]:
            break
        answer.append(v[i][1])
    print(*answer[::-1])