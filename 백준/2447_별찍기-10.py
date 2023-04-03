def star(pattern):
    arr = []
    n = len(pattern)
    for i in range(3*n):
        if i//n == 1:
            arr.append(pattern[i%n]+" "*n+pattern[i%n])
        else:
            arr.append(pattern[i%n]*3)
    return arr

n = int(input())
pattern = ["***","* *","***"]
k = 0
while n > 3:
    k += 1
    n //= 3
for _ in range(k):
    pattern = star(pattern)
for x in pattern:
    print(x)