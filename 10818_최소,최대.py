n = int(input())
lst = list(map(int,input().split()))
# print(min(lst),max(lst))
min_v = int(1e6)
max_v = int(-1e6)
for i in range(n):
    if lst[i] < min_v:
        min_v = lst[i]
    if lst[i] > max_v:
        max_v = lst[i]
print(min_v,max_v)