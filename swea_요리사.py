from itertools import combinations

T = int(input())
for tc in range(T):
    n = int(input())
    s = [list(map(int,input().split())) for _ in range(n)]
    lst = [i for i in range(0,n)]
    ans = 1e9
    for x in combinations(lst,n//2):
        if 0 not in x:
            break
        a = 0
        b = 0
        v = [0] * n
        for idx in x:
            v[idx] = 1
        for i in range(n):
            for j in range(n):
                if v[i] == 1 and v[j] == 1:
                    a += s[i][j]
                elif v[i] == 0 and v[j] == 0:
                    b += s[i][j]
        if abs(a-b) < ans:
            ans = abs(a-b)
    print(f'#{tc+1}',ans)