import sys, heapq
input = sys.stdin.readline
inf = int(1e9)

n,m = map(int,input().split())
lst = [[] for _ in range(n+1)]
dis = [inf] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    lst[a].append((b,c))
    lst[b].append((a,c))

def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))
    
    while q:
        d,now = heapq.heappop(q)

        if dis[now] < d:
            continue
        for i in lst[now]:
            cost = d + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)
print(dis[n])
