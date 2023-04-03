from collections import defaultdict, deque

n = int(input())
m = int(input())
computers = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    computers[a].append(b)
    computers[b].append(a)

cnt = 0
v = [0] * (n+1)
q = deque()
q.append(1)
v[1] = 1
while q:
    x = q.popleft()
    for i in computers[x]:
        if v[i] == 0:
            q.append(i)
            v[i] = 1
            cnt += 1
print(cnt)