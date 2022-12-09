from collections import defaultdict, deque

while 1:
    n,k = map(int,input().split())
    if n == 0:
        break
    lst = list(map(int,input().split()))
    parents = defaultdict(int)
    q = deque([lst[0]])
    ans = 0
    for i in range(1,n):
        if lst[i] != lst[i-1] + 1:
            x = q.popleft()      
        q.append(lst[i])
        parents[lst[i]] = x

    grand = parents[parents[k]]
    parent = parents[k]
    if grand == 0:
        print(0)
    else:
        for p in list(parents):
            if parents[p] != parent and parents[parents[p]] == grand:
                ans += 1
        print(ans)