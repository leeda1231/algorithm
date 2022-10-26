from collections import deque

def solution(arr):
    answer = []
    q = deque(arr)
    last = arr[0]
    answer.append(arr[0])
    while q:
        x = q.popleft()
        if x != last:
            answer.append(x)
            last = x
    return answer