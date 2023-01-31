n,m = map(int,input().split())
s = []
v = [0]*(n+1)

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if v[i] == 0:
            s.append(i)
            v[i] = 1
            dfs()
            s.pop()
            v[i] = 0

dfs()