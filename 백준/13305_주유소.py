n = int(input())
road = list(map(int,input().split()))
gas = list(map(int,input().split()))
min_val = gas[0]
answer = 0

for i in range(n-1):
    if min_val > gas[i]:
        min_val = gas[i]
    answer += min_val * road[i]

print(answer)