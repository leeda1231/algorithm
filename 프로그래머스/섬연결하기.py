# 최소 신장 트리 => 크루스칼 알고리즘
def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    
    # 주어진 모든 간선 정보에 대해 간선 비용이 낮은 순서(오름차순)로 정렬
    costs = sorted(costs, key = lambda x: x[2])
    for x,y,cost in costs:
        if find(parent,x) != find(parent,y):
            union(parent,x,y)
            print(parent)
            answer += cost
            
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(n, costs)