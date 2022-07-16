n = int(input())
lst = []
# 자릿수 구하기
while n:
    lst.append(n%10)
    n //= 10

a = 0
b = 0
for i in range(len(lst)//2):
    a += lst[i]
    b += lst[-i-1]

if a == b:
    print('LUCKY')
else:
    print('READY')