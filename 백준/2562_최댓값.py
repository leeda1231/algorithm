n = 0
m = 0
for i in range(1,10):
    x = int(input())
    if x > n:
        n = x
        m = i
print(n)
print(m)