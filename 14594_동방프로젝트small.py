n = int(input())
m = int(input())
lst = [1]*(n+1)
for _ in range(m):
    x,y = map(int,input().split())
    for i in range(x,y):
        lst[i] = 0

print(n-lst.count(0))