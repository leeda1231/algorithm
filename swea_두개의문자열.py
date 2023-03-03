T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = int(-10e6)
    if n < m:
        for i in range(m-n+1):
            ans = max(ans,sum([x*y for x,y in zip(a,b[i:i+n])]))
    else:
        for j in range(n-m+1):
            ans = max(ans,sum([x*y for x,y in zip(a[j:j+m],b)]))
    print(f'#{tc+1} {ans}')