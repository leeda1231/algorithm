# DFS
def dfs(num,i,numbers,target):
    global answer
    if i == n:
        if num == target:
            answer += 1
        return
    dfs(num+numbers[i],i+1,numbers,target)
    dfs(num-numbers[i],i+1,numbers,target)
        
    

def solution(numbers, target):
    global n, answer
    answer = 0
    n = len(numbers)
    dfs(numbers[0],1,numbers,target)
    dfs(-numbers[0],1,numbers,target)
    return answer


# BFS
from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append((1,numbers[0]))
    q.append((1,-numbers[0]))
    while q:
        i,num = q.popleft()
        if i == n:
            if num == target:
                answer += 1
        else:
            q.append((i+1,num+numbers[i]))
            q.append((i+1,num-numbers[i]))    
    return answer