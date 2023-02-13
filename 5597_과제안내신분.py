s = {i for i in range(1,31)}
for _ in range(28):
    x = {int(input())}
    s -= x
lst = list(s)
lst.sort()
print(lst[0])
print(lst[1])