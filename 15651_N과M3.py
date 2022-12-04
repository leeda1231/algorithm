n,m = map(int,input().split())
s = []

def dfs(s):
    if len(s) == m:
        print(' '.join(map(str,s))) # join은 int형 안됨
        return
       
    for i in range(1,n+1):
        dfs(s+[i])

dfs([])