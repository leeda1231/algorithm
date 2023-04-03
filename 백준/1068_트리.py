from collections import defaultdict

n = int(input())
parents = list(map(int,input().split()))
k = int(input())

graph = defaultdict(list)
for i in range(n):
    if parents[i] == -1:
        idx = i
    else:
        if i != k:
            graph[parents[i]].append(i)

def dfs(node):
    global cnt
    if not graph[node]:
        cnt += 1
        return
    for x in graph[node]:
        dfs(x)

if k == idx:
    print(0)
else:
    cnt = 0
    dfs(idx)
    print(cnt)