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

'''
# itertools

from itertools import permutations
n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]
res = list(permutations(lst,m))

for i in res:
    print(' '.join(map(str,i)))
'''


# n,m = map(int,input().split())

# def dfs(s):
#     if len(s) == m:
#         print(' '.join(map(str,s))) # join은 int형 안됨
#         return
    
#     for i in range(1,n+1):
#         if i in s:
#             continue
#         dfs(s+[i])

# dfs([])

'''
# itertools

from itertools import permutations

n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]
res = list(permutations(lst,m))

for i in res:
    for j in i:
        print(j,end=' ')
    print()
'''
