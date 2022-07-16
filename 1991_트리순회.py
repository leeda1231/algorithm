n = int(input())
nodes = {}

for _ in range(n):
    m, l, r = input().split()
    nodes[m] = {'left': l, 'right': r}

def preorder(node):
    print(node, end='')
    if nodes[node]['left'] != '.':
        preorder(nodes[node]['left'])
    if nodes[node]['right'] != '.':
        preorder(nodes[node]['right'])

def inorder(node):
    if nodes[node]['left'] != '.':
        inorder(nodes[node]['left'])
    print(node, end='')
    if nodes[node]['right'] != '.':
        inorder(nodes[node]['right'])

def postorder(node):
    if nodes[node]['left'] != '.':
        postorder(nodes[node]['left'])
    if nodes[node]['right'] != '.':
        postorder(nodes[node]['right'])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')