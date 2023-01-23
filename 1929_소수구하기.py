m,n = map(int,input().split())
sieve = [1] * 1000001
sieve[1] = 0
k = int(1000000**0.5)
for i in range(2,k+1):
    if sieve[i]:
        for j in range(i+i,n+1,i):
            sieve[j] = 0

for i in range(m,n+1):
    if sieve[i]:
        print(i)