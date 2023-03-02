T = int(input())
for tc in range(T):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    v = [0] * (n+1)
    for num in nums:
        v[num] = 1
    ans = []
    for i in range(1,n+1):
        if v[i] == 0:
           ans.append(i)
    print(f'#{tc+1} {" ".join(map(str,ans))}')