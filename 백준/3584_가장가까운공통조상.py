import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
from collections import defaultdict

def dfs(x,depth):
    v[x] = 1
    for y in graph[x]:
        if v[y] == 1:
            continue
        d[y] = depth + 1
        dfs(y,depth+1)

def lca(a,b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parents[a]
        else:
            b = parents[b]
    while a != b:
        a = parents[a]
        b = parents[b]
    return a 

T = int(input())
for _ in range(T):
    n = int(input())
    parents = [0] * (n+1)
    d = [0] * (n+1)
    v = [0] * (n+1)
    graph = defaultdict(list)
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        parents[b] = a
    for i in range(1,n+1):
        if parents[i] == 0:
            root = i
            break
    dfs(root,0)
    a,b = map(int,input().split())
    print(lca(a,b))