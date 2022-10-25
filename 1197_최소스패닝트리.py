def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

v,e = map(int,input().split())
tree = []
parent = [i for i in range(v+1)]
answer = 0
for _ in range(e):
    a,b,c = map(int,input().split())
    tree.append([a,b,c])
tree.sort(key = lambda x:x[2])

for x,y,w in tree:
    if find(parent,x) != find(parent,y):
        union(parent,x,y)
        answer += w
    
print(answer)