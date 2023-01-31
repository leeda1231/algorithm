T = int(input())
for tc in range(T):
    bar = list(input())
    cnt = 1
    ans = 0
    for i in range(1,len(bar)):
        if bar[i] == '(':
            cnt += 1
        # laser
        elif bar[i-1] == '(':
            cnt -= 1
            ans += cnt
        else:
            cnt -= 1
            ans += 1

    print(f'#{tc+1}',ans)