def n_queen(s):
    global ans
    if s == n+1:
        ans += 1
        return
    for i in range(1,n+1):
        lst[s] = i
        for j in range(1,s):
            if lst[s] == lst[j] or abs(lst[s]-lst[j]) == s-j:
                break
        else:
            n_queen(s+1)

T = int(input())
for tc in range(T):
    n = int(input())
    ans = 0
    lst = [0] * (n+1)
    n_queen(1)
    print(f'#{tc+1} {ans}')