T = int(input())
for tc in range(T):
    n = int(input())
    prices = list(map(int,input().split()))
    ans = 0
    max_val = prices[n-1]
    for i in range(n-2,-1,-1):
        if prices[i] > max_val:
            max_val = prices[i]
        elif prices[i] < max_val:
            ans += max_val - prices[i]
    print(f'#{tc+1}',ans)