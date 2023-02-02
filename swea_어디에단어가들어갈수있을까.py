T = int(input())
for tc in range(T):
    ans = 0
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # 가로
    for i in range(n):
        lst = arr[i] + [0]
        for j in range(1,n+1):
            if lst[j] == 1 and lst[j-1] != 0:
                lst[j] += lst[j-1]
            elif lst[j] == 0:
                if lst[j-1] == k:
                    ans += 1
    # 세로
    arr2 = list(zip(*arr))
    for i in range(n):
        lst = arr2[i]
        cnt = 0
        for j in range(n):
            if lst[j] == 1:
                cnt += 1
            elif lst[j] == 0:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1
    print(f'#{tc+1}',ans)