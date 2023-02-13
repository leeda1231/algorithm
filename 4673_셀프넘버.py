v = [0] * 10001
def d(n):
    new = n
    while n != 0:
        new += n % 10
        n //= 10
    if new > 10000 or v[new] == 1:
        return
    v[new] = 1
    d(new)

for i in range(1,10001):
    d(i)

for i in range(1,10001):
    if v[i] == 0:
        print(i)