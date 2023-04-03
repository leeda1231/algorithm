a,b = map(int,input().split())
c = int(input())
n = int(input())
if a > c:
    print(0)
else:
    if a*n+b > c*n:
        print(0)
    else:
        print(1)