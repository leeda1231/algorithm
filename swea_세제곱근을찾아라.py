#1
T = int(input())
for tc in range(T):
    n = int(input())
    x = round(n ** (1/3),2) # 부동소수점 오차 때문
    if x == int(x):
        print(f'#{tc+1} {int(x)}')
    else:
        print(f'#{tc+1}',-1)


#2
from collections import defaultdict

numbers = defaultdict(lambda:-1)
x = 1
while 1:
    y = x**3
    if y > 1e18:
        break
    numbers[y] = x
    x+= 1

T = int(input())
for tc in range(T):
    n = int(input())
    print(f'#{tc+1}',numbers[n])