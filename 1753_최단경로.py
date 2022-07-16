import sys, heapq
input = sys.stdin.readline
inf = int(1e9)

v,e = map(int,input().split())
s = int(input())
lst = [[] for _ in range(v+1)]
dis = [inf] * (v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    lst[a].append((b,c))

def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))
    dis[s] = 0
    while q:
        d,now = heapq.heappop(q)
        # 방문처리 대신(최단경로)
        if dis[now] < d:
            continue
        for i in lst[now]:
            cost = d + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(s)

for i in dis[1:]:
    if i == inf:
        print('INF')
    else:
        print(i)
