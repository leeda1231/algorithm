n = int(input())
lines = list(map(int,input().split()))
lines.sort()
answer = 0
last = 0
for i in range(n):
    lines[i] += last
    answer += lines[i]
    last = lines[i]
print(answer)