from collections import defaultdict, deque

def bfs():
    q = deque([(s,0)])
    v = [0] * 101
    v[s] = 1
    depth[0].append(s)
    while q:
        x,d = q.popleft()
        for i in contact[x]:
            if v[i] == 0:
                q.append((i,d+1))
                v[i] = 1
                depth[d+1].append(i)
    return d

for tc in range(10):
    n,s = map(int,input().split())
    data = list(map(int,input().split()))
    contact = defaultdict(set)
    depth = defaultdict(list)
    for i in range(0,n,2):
        contact[data[i]].add(data[i+1])
    d = bfs()
    print(f'#{tc+1}',max(depth[d]))