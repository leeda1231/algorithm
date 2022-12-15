from collections import defaultdict
n,m = map(int,input().split())
ladders = defaultdict(int)
snakes = defaultdict(int)
for _ in range(n):
    x,y = map(int,input().split())
    ladders[x] = y
for _ in range(m):
    u,v = map(int,input().split())
    snakes[u] = v

