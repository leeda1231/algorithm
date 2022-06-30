from collections import defaultdict
import sys, heapq
input = sys.stdin.readline
inf = int(1e9)

n,m = map(int,input().split())
graph = defaultdict(dict)
for _ in range(m):
    a,b,c = map(int,input().split())
    # 중첩 딕셔너리
    graph[a][b] = c
    graph[b][a] = c
s,t = map(int,input().split())
dis = [inf] * (n+1)

def dijkstra(graph, s):
    q = []
    heapq.heappush(q,(0,s))
    dis[s] = 0
    while q:
        d, now = heapq.heappop(q)
        
        # 이미 들렀던 부분(최소로)
        if dis[now] < d:
            continue

        for new, new_d in graph[now].items():
            cost = d + new_d
            if cost < dis[new]:
                dis[new] = cost
                heapq.heappush(q,(cost,new))

dijkstra(graph,s)
print(dis[t])