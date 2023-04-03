import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

preorder = []
while 1:
    try:
        preorder.append(int(input()))
    except:
        break

