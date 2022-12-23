while 1:
    x,y = map(int,input().split())
    if x == 0:
        break
    if x > y:
        print('Yes')
    else:
        print('No')