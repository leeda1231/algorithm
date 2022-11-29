n = int(input())
lst = []
answer = 0
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

for i in range(n):
    if lst[i] - i < 0:
        break
    answer += lst[i] - i

print(answer)