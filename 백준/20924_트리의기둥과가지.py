# 나무의 기둥의 길이 & 가장 긴 가지의 길이
# 기둥 : 루트 노드에서부터 기가 노드까지
# 가지 : 기가 노드에서부터 임의의 리프 노드까지
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,r = map(int,input().split())
graph = defaultdict(list)
v = [0] * (n+1)
giga = 0

# 기둥
def dfs(node,c):
    global giga,giga_l
    v[node] = 1
    cnt = 0
    giga_l = c
    for x,y in graph[node]:
        if v[x] == 1:
            continue
        cnt += 1
        tmp_n,tmp_c = x,y
    if cnt > 1:
        giga = node
        return
    if cnt == 1:
        dfs(tmp_n,c+tmp_c)

# 가장 긴 가지
def dfs2(node,val):
    global max_val
    v[node] = 1
    if len(graph[node]) == 1:
        if max_val < val:
            max_val = val
        return
    for x,y in graph[node]:
        if v[x] == 1:
            continue
        dfs2(x,val+y)


for _ in range(n-1):
    a,b,d = map(int,input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

dfs(r,0)
max_val = 0
if giga == 0:
    print(giga_l,0)
else:
    dfs2(giga,0)
    print(giga_l,max_val)