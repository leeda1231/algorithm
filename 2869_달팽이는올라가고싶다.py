a,b,v = map(int,input().split())
if v == a:
    print(1)
else:
    d = a-b
    v-= a
    q = v//d
    if v%d == 0:
        print(1+q)
    else:
        print(2+q)