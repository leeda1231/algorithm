T = int(input())
for tc in range(T):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)
    ans = sum(lst[:k])
    print(f'#{tc+1} {ans}')