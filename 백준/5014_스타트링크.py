from collections import deque
# f: 최고층, s: 현재층, g: 스타트링크, u: 위로, d: 아래로
f,s,g,u,d = map(int,input().split())
answer = 'use the stairs'
q = deque()
q.append((0,s))
v = [0] * (f+1)
v[s] = 1
while q:
    cnt,floor = q.popleft()
    if floor == g:
        answer = cnt
        break
    if u and d:
        for move in [u,-d]:
            if 0 < floor + move <= f and v[floor+move] == 0:
                q.append((cnt+1,floor+move))
                v[floor+move] = 1
    elif u:
        if 0 < floor + u <= f and v[floor+u] == 0:
                q.append((cnt+1,floor+u))
                v[floor+u] = 1
    elif d:
        if 0 < floor - d <= f and v[floor-d] == 0:
                q.append((cnt+1,floor-d))
                v[floor-d] = 1
    
print(answer)