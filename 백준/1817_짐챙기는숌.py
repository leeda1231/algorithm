n,m = map(int,input().split())
answer = 0
if n == 0:
    print(answer)
else:
    books = list(map(int,input().split()))
    w = 0
    answer = 1
    for b in books:
        w += b
        if w <= m:
            continue
        else:
            answer += 1
            w = b
    print(answer)