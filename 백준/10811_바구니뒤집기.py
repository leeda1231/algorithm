n,m = map(int,input().split())
baskets = [i for i in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    baskets[i:j+1] = baskets[j:i-1:-1]
print(*baskets[1:])