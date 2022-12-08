import sys
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)
d = [0] * (n+1)
v = [0] * (n+1)

def dfs(x,depth):
    v[x] = 1
    d[x] = depth
    for y in graph[x]:
        if v[y] == 1:
            continue
        parent[y] = x
        dfs(y,depth+1)

def lca(a,b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1,0)
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))