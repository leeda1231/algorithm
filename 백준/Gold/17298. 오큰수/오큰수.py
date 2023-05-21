n = int(input())
lst = list(map(int,input().split()))
stack = [[0,lst[0]]]
ans = [-1] * n
for i in range(1,n):
    while stack and stack[-1][1] < lst[i]:
        idx,v = stack.pop()
        ans[idx] = lst[i]
    stack.append([i,lst[i]])
print(*ans)