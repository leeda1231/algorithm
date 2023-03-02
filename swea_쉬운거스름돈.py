T = int(input())
for tc in range(T):
    n = int(input())
    money = [50000,10000,5000,1000,500,100,50,10]
    ans = []
    for m in money:
        if m <= n:
            ans.append(n//m)
            n %= m
        else:
            ans.append(0)
    print(f'#{tc+1}')
    print(*ans)