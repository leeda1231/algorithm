from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
#왼루오
k = int(input())
lst = list(map(int,input().split()))
trees = defaultdict(list)
start = 0
end = len(lst) - 1

def dfs(start,end,d):
    global trees
    if start > end:
        return
    mid = (start+end) // 2
    trees[d].append(lst[mid])
    dfs(start,mid-1,d+1)
    dfs(mid+1,end,d+1)

dfs(start,end,0)
for tree in trees:
    print(*trees[tree])