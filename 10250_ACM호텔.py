T = int(input())
for tc in range(T):
    h,w,n = map(int,input().split())
    f = n % h
    b = n//h + 1
    if f == 0:
        f += h
        b -= 1
    print(100*f+b)