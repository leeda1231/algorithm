for tc in range(10):
    n = int(input())
    buildings = list(map(int,input().split()))
    ans = 0
    # 왼쪽 2개 max 오른쪽 2개 max
    left = 0
    if n == 4:
        right = 0
    else:
        right = max(buildings[3],buildings[4])
    for i in range(2,n-3):
        if buildings[i] > left and buildings[i] > right:
            ans += buildings[i] - max(left,right)
        left = max(buildings[i-1],buildings[i])
        right = max(buildings[i+2],buildings[i+3])
    if buildings[n-3] > left:
        ans += buildings[n-3] - left
    
    print(f'#{tc+1}',ans)