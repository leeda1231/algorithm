from collections import deque

def solution(people, limit):
    n = len(people)
    people.sort()
    q = deque(people)
    answer = 0
    while q:
        end = q.pop()
        answer += 1
        if not q:
            break
        if q[0] + end <= limit:
            q.popleft()
            
    return answer