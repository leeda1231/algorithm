from collections import deque

def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    order = 0
    priorities.sort(reverse=True)
    while q:
        x,y = q.popleft()
        if x == priorities[order]:
            order += 1
            if y == location:
                return order
        else:
            q.append((x,y))