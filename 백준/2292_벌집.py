n = int(input())
num = 1
d = 1
while 1:
    if n <= num:
        print(d)
        break
    num += 6*d
    d += 1