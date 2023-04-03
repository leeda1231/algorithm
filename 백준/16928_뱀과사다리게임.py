from collections import defaultdict, deque
n,m = map(int,input().split())
ladders = defaultdict(int)
snakes = defaultdict(int)
for _ in range(n):
    x,y = map(int,input().split())
    ladders[x] = y
for _ in range(m):
    u,v = map(int,input().split())
    snakes[u] = v

q = deque([1])
v = [0] * 101
cnt = [0] * 101
v[1] = 1

while q:
    x = q.popleft()
    if x == 100:
        break
    for i in range(1,7):
        if x + i <= 100 and v[x+i] == 0:
            v[x+i] = 1
            cnt[x+i] = cnt[x] + 1
            # 사다리
            if ladders[x+i]:
                if v[ladders[x+i]] == 0:
                    v[ladders[x+i]] = 1
                    cnt[ladders[x+i]] = cnt[x] + 1
                    q.append(ladders[x+i])
            # 뱀
            elif snakes[x+i]:
                if v[snakes[x+i]] == 0:
                    v[snakes[x+i]] = 1
                    cnt[snakes[x+i]] = cnt[x] + 1
                    q.append(snakes[x+i])
            # 보드
            else:
                q.append(x+i)

print(cnt[100])