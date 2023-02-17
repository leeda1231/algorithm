import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    a,n = input().rstrip().split()
    lst.append((int(a),n,i))
lst.sort(key=lambda x:(x[0],x[2]))
for x,y,z in lst:
    print(x,y)