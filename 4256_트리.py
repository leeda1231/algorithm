import sys
input = sys.stdin.readline
T = int(input())

def dfs(preorder,inorder):
    if not preorder:
        return   
    node = preorder[0]
    idx = inorder.index(node)
    dfs(preorder[1:1+idx],inorder[:idx])
    dfs(preorder[1+idx:],inorder[idx+1:])
    print(node,end=' ')

for _ in range(T):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    dfs(preorder,inorder)
    print()