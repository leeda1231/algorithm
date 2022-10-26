from collections import deque

def solution(s):
    answer = True
    q = deque(s)
    new_q = deque()
    while q:
        x = q.popleft()
        if x == "(":
            new_q.append(x)
        else:
            if new_q:
                new_q.pop()
            else:
                return False
    if new_q:
        return False

    return True