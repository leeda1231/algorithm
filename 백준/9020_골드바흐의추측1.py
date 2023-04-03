T = int(input())
prime = [1] * 10001
prime[0] = 0
prime[1] = 0
for i in range(2,10001):
    if prime[i]:
        for j in range(i+i,10001,i):
            prime[j] = 0

for _ in range(T):
    n = int(input())
    x = n//2
    for i in range(x,1,-1):
        if prime[i] == 1 and prime[n-i] == 1:
            print(i,n-i)
            break
    