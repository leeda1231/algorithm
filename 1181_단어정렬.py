n = int(input())
lst = []
for _ in range(n):
    word = input()
    lst.append((len(word),word))
lst.sort()
tmp = ''
for l in lst:
    if tmp != l[1]:
        print(l[1])
        tmp = l[1]