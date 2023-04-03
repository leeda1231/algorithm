#2
n = int(input())
q = n//5
while q:
    if (n-q*5)%3 == 0:
        print(q+(n-q*5)//3)
        break
    q -= 1
else:
    if n % 3 == 0:
        print(n//3)
    else:
        print(-1)