n = int(input())
scores = []
answer = 0
for _ in range(n):
    scores.append(int(input()))
for i in range(n-2,-1,-1):
    if scores[i+1] > scores[i]:
        continue
    answer += scores[i] - scores[i+1] + 1
    scores[i] = scores[i+1] - 1

print(answer)