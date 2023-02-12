def dfs(x):
    if graph[x][0] == '+':
        return dfs(graph[x][1]) + dfs(graph[x][2])
    if graph[x][0] == '-':
        return dfs(graph[x][1]) - dfs(graph[x][2])
    if graph[x][0] == '*':
        return dfs(graph[x][1]) * dfs(graph[x][2])
    if graph[x][0] == '/':
        return dfs(graph[x][1]) // dfs(graph[x][2])
    return graph[x][0]

for tc in range(10):
    n = int(input())
    graph = {}
    for _ in range(n):
        i,*lst = input().split()
        if len(lst) == 1:
            graph[i] = list(map(int,lst))
        else:
            graph[i] = lst
    ans = dfs('1')
    print(f'#{tc+1}',ans)