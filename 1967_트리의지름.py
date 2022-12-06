from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
answer = 0
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

def dfs(node,length):
    global max_node, max_val
    for n,l in tree[node]:
        if v[n] == 1:
            continue
        v[n] = 1
        tmp = length + l
        if tmp > max_val:
            max_val = tmp
            max_node = n
        dfs(n,tmp)
        
v = [0] * (n+1)
v[1] = 1
max_node = 0
max_val = 0
dfs(1,0)
v = [0] * (n+1)
v[max_node] = 1
dfs(max_node,0)

print(max_val)