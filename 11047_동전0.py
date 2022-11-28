n,k = map(int,input().split())
coins = []
answer = 0
for _ in range(n):
    coins.append(int(input()))
for i in range(1,n+1):
    if k == 0:
        break
    if coins[-i] <= k:
        answer += k // coins[-i]
        k = k % coins[-i] 

print(answer)