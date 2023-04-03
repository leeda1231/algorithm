T = int(input())
for _ in range(T):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    planet = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for x,y,r in planet:
        d1 = ((x1-x)**2 + (y1-y)**2)**0.5
        d2 = ((x2-x)**2 + (y2-y)**2)**0.5
        if d1 < r and d2 < r:
            continue
        if d1 < r:
            ans += 1
        elif d2 < r:
            ans += 1
    print(ans)