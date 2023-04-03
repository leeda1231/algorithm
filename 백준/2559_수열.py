N, K = map(int,input().split())
lst = list(map(int,input().split()))
maxV = total = sum(lst[:K])

for i in range(N-K):
    total = total - lst[i] + lst[K+i] 
    if maxV < total:
        maxV = total

print(maxV)

'''
제한시간 1초면
for
    sum
쓰면 시간초과 뜬다
'''