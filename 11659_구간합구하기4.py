import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [0] + list(map(int,input().split()))
for i in range(1,n+1):
    lst[i] += lst[i-1]

for _ in range(m):
    i,j = map(int,input().split())
    ans = lst[j] - lst[i-1]
    print(ans)