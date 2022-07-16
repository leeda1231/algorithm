def dfs(x,cnt):
    global ans
    v[x] = 1
    if cnt == 5:
        ans = 1
        return
    for i in lst[x]:
        if v[i] == 0:
            dfs(i,cnt+1)
            v[i] = 0 # 얘가 중요. 다음탐색위해 다시 0으로


n,m = map(int,input().split())
lst = [[] for _ in range(n)]
ans = 0

for _ in range(m):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(n):
    lst[i] = list(set(lst[i]))

for i in range(n):
    v = [0]*n
    dfs(i,1)
    
print(ans)

'''
참고자료
https://grini25.tistory.com/110
'''