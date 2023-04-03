n,m = map(int,input().split())
baskets = [i for i in range(1,n+1)]
for _ in range(m):
    i,j,k = map(int,input().split())
    i -= 1
    j -= 1
    k -= 1
    baskets[i:j+1] = baskets[k:j+1] + baskets[i:k]
print(*baskets)