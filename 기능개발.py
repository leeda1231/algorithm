import math
from collections import deque

def solution2(progresses, speeds):
    answer = []
    work = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    print(work)
    q = deque(work)
    longDay = q[0]
    day = 0
    while q:
        x = q.popleft()
        if x > longDay:
            longDay = x
            answer.append(day)
            day = 1
        else:
            day += 1
    answer.append(day)          
    return answer


def solution1(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[i] < 100:
                if cnt != 0:
                    answer.append(cnt)
                break
            else:
                cnt += 1
        progresses = progresses[cnt:]
        speeds = speeds[cnt:]
        if not progresses:
            answer.append(cnt)
    return answer