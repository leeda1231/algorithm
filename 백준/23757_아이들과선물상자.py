import heapq

n,m = map(int,input().split())
c = list(map(int,input().split()))
w = list(map(int,input().split()))
ans = 1
present = []
for x in c:
    heapq.heappush(present,-x)

for x in w:
    p = -heapq.heappop(present)
    if x > p:
        ans = 0
        break
    elif x < p:
        heapq.heappush(present,x-p)

print(ans)