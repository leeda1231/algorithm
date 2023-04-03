#2
n = int(input())
for i in range(2,n+1):
    while n%i==0:
        print(i)
        n //= i


#1
def result(n):
    for i in range(2,n+1):
        if primes[i] == 1:
            if n == i:
                print(i)
                return
            while n%i==0:
                print(i)
                n //= i

n = int(input())
primes = [1] * (n+1)
primes[1] = 0
m = int(n**0.5)
for i in range(2,m+1):
    if primes[i]:
        for j in range(i+i,n+1,i):
            primes[j] = 0

result(n)