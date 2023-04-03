C = int(input())
for _ in range(C):
    n,*lst = map(int,input().split())
    mean = sum(lst) / n
    cnt = 0
    for l in lst:
        if l > mean:
            cnt += 1
    print("%0.3f"%(cnt/n*100)+"%")