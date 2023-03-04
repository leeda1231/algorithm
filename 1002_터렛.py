T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    X = (x1-x2)**2
    Y = (y1-y2)**2
    Z = (X+Y)**0.5
    R1 = r1+r2
    R2 = abs(r2-r1)
    if x1 == x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif Z == R1 or Z == R2:
        print(1)
    elif R2 < Z < R1:
        print(2)
    else:
        print(0)