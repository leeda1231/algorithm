def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x%y)

T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    print(a*b//gcd(a,b))