m = int(input())
n = int(input())

prime = [1] * 10001
prime[1] = 0
for i in range(2,10001):
    if prime[i]:
        for j in range(i+i,10001,i):
            prime[j] = 0

total = 0
min_val = 10000
for num in range(m,n+1):
    if prime[num]:
        if min_val > num:
            min_val = num
        total += num

if total == 0:
    print(-1)
else:    
    print(total)
    print(min_val)