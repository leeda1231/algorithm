n,m = map(int,input().split())
baskets = [i for i in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    baskets[i],baskets[j] = baskets[j],baskets[i]
print(*baskets[1:])