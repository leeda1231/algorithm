a,b = map(int,input().split())
c = int(input())

b += c
if b < 60:
    print(a,b)
else:
    a += b//60
    a %= 24
    b %= 60
    print(a,b)