T = int(input())
for _ in range(T):
    j,n = map(int,input().split())
    weights = []
    for _ in range(n):
        r,c = map(int,input().split())
        weights.append(r*c)

    weights.sort(reverse=True)

    total = 0
    cnt = 0
    for weight in weights:
        cnt += 1
        total += weight
        if total >= j:
            break
    
    print(cnt)