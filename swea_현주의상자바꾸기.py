T = int(input())
for tc in range(T):
    n,q = map(int,input().split())
    lst = [0]*n
    for i in range(1,q+1):
        l,r = map(int,input().split())
        for j in range(l-1,r):
            lst[j] = i
    print(f'#{tc+1} {" ".join(map(str,lst))}')
    # print(f'#{tc+1}',*lst) f-string은 *이 안되기 때문