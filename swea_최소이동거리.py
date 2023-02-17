from collections import defaultdict, deque

inf = int(1e9)
T = int(input())
for tc in range(T):
    n,E = map(int,input().split())
    graph = defaultdict(list)
    v = [inf] * (n+1)
    v[0] = 0
    for _ in range(E):
        s,e,w = map(int,input().split())
        graph[s].append((e,w))
    q = deque()
    q.append(0)
    while q:
        x = q.popleft()
        for e,w in graph[x]:
            if v[e] > v[x]+w:
                v[e] = v[x] + w
                q.append(e)
    print(f'#{tc+1}',v[-1])