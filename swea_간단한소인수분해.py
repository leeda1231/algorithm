T = int(input())
for tc in range(T):
    n = int(input())
    prime = [2,3,5,7,11]
    ans = [0,0,0,0,0]
    for i in range(5):
        while n%prime[i]==0:
            n//=prime[i]
            ans[i]+= 1

    print(f'#{tc+1}',*ans)