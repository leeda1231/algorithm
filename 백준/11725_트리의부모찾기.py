from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = defaultdict(list)
parents = [0] * (n+1)
parents[1] = 1
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(n):
    for x in tree[n]:
        if parents[x] != 0:
            continue
        parents[x] = n
        dfs(x)

dfs(1)
print(*parents[2:],sep='\n')