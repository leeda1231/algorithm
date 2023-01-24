import sys
input = sys.stdin.readline

def prime_cnt(n):
    ans = 0
    prime = [1] * (2*n+1)
    m = int((2*n)**0.5)
    for i in range(2,m+1):
        if prime[i]:
            for j in range(i+i,2*n+1,i):
                prime[j] = 0
    for i in range(n+1,2*n+1):
        if prime[i]:
            ans += 1    
    return ans

while 1:
    n = int(input())
    if n == 0:
        break
    print(prime_cnt(n))