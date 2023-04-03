import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

n = int(input())
a,b,c = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d,e,l = map(int,input().split())
    graph[d].append((e,l))
    graph[e].append((d,l))

def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))
    dis[s] = 0
    while q:
        d,now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

min_val = inf
ans = 0
for i in range(1,n+1):
    if i != a and i != b and i != c:
        dis = [inf] * (n+1)
        dijkstra(i)
        if min_val > dis[a]:
            ans = i
            min_val = dis[a]
        if min_val > dis[b]:
            ans = i
            min_val = dis[b]
        if min_val > dis[c]:
            ans = i
            min_val = dis[c]

print(ans)
            
