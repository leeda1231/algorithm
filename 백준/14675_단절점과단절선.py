from collections import defaultdict
import sys
input = sys.stdin.readline
graph = defaultdict(list)

n = int(input())
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
for _ in range(q):
    t,k = map(int,input().split())
    if t == 1:
        if len(graph[k]) > 1:
            print('yes')
        else:
            print('no')
    else:
        print('yes')