from itertools import combinations

n,m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))


ans = 1e9
for chick in combinations(chicken, m):
    dis = 0
    for h in home:
        dis_h = 1e9
        for c in chick:
            dis_h = min(dis_h, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        dis += dis_h
    ans = min(ans, dis)

print(ans)

# 시간초과
# def dfs(cnt):
#     global ans
#     if cnt == k-m:
#         dis()
#         return
#     for i in range(n):
#         for j in range(n):
#             if city[i][j] == 2:
#                 city[i][j] = 0
#                 chicken.remove((i,j))
#                 dfs(cnt+1)
#                 city[i][j] = 2
#                 chicken.append((i,j))

# def dis():
#     global ans
#     total = 0
#     for h in home:
#         dis_h = 1e9
#         for c in chicken:
#             dis_h = min(dis_h, abs(h[0] - c[0]) + abs(h[1] - c[1]))
#         total += dis_h
#         if total > ans:
#             return
#     ans = min(ans, total)
#     return

# ans = 1e9
# dfs(0)
# print(ans)

# 첫번째 풀이
# from itertools import combinations

# n, m = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]

# h = []
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1:
#             h.append((i,j))

# c = []
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 2:
#             c.append((i,j))

# ans = 10000
# for i in combinations(c,m):
#     dis = 0
#     for j in h:
#         dis_h = 100
#         for k in i:
#             dis_h = min(dis_h,abs(k[0]-j[0])+abs(k[1]-j[1]))
#         dis += dis_h
#     ans = min(dis,ans)

# print(ans)