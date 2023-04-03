n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
total = 0
for i in range(n):
    if i % 3 == 2:
        continue
    total += lst[i]

print(total)