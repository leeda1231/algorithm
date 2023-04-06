from collections import deque

def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    answer = 0
    q = deque([0]*bridge_length)
    total = 0
    for i in range(n):
        while 1:
            tmp = q.pop()
            total -= tmp
            if total + truck_weights[i] <= weight:
                total += truck_weights[i]
                q.appendleft(truck_weights[i])
                answer += 1
                break
            else:
                q.appendleft(0)
                answer += 1
    
    answer += len(q)
        
    return answer