from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,w = map(int,input().split())
graph = defaultdict(list)
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
v = defaultdict(int)

leaf_cnt = 0
def dfs(node):
    global leaf_cnt
    v[node] = 1
    if len(graph[node]) == 1 and node != 1:
        leaf_cnt += 1
        return
    for x in graph[node]:
        if v[x] == 0:
            dfs(x)

dfs(1)
print(w/leaf_cnt)