a = set(i for i in range(1,31))
b = set()
for _ in range(28):
    b.add(int(input()))
lst = list(a-b)
lst.sort()
for i in lst:
    print(i)