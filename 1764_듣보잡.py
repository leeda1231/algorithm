import sys
input = sys.stdin.readline

n,m = map(int,input().split())
l = set()
for _ in range(n):
    l.add(input().rstrip())
s = set()
for _ in range(m):
    s.add(input().rstrip())
lst = list(l&s)
lst.sort()
print(len(lst))
for v in lst:
    print(v)