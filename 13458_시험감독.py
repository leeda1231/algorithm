n = int(input())
students = list(map(int,input().split()))
b,c = map(int,input().split())
answer = 0
for a in students:
    if (a - b) <= 0:
        answer += 1
        continue
    if (a - b) % c:
        answer += 2 + (a - b) // c
    else:
        answer += 1 + (a - b) // c
print(answer)