def num(n,lst):
    ans = []
    for i in range(n-1):
        for j in range(i+1,n):
            x = lst[i]*lst[j]
            tmp = 10
            while x:
                y = x%10
                if tmp < y:
                    break
                tmp = y
                x //= 10
            else:
                ans.append(lst[i]*lst[j])
    if ans:
        return max(ans)
    return -1

T = int(input())
for tc in range(T):
    n = int(input())
    lst = list(map(int,input().split()))
    print(f'#{tc+1} {num(n,lst)}')