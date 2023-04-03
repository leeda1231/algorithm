# 에라스토테네스의 체
n = int(input())
lst = list(map(int,input().split()))
ans = 0
prime = [1] * 1001
prime[1] = 0
m = int(1000**0.5) # 제곱근까지만 약수의 여부
for i in range(2,m+1):
    if prime[i]:
        for j in range(i+i,1001,i):
            prime[j] = 0

for num in lst:
    if prime[num] == 1:
        ans += 1

print(ans)