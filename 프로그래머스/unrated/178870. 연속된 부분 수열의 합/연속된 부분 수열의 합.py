def solution(sequence, k):
    n = len(sequence)
    sequence = [0] + sequence
    for i in range(n):
        sequence[i+1] += sequence[i]
    lst = []
    start = 0
    end = 1
    while end < n+1:
        num = sequence[end] - sequence[start]
        if num == k: 
            lst.append([end-start,start,end-1])
            end += 1
        elif num < k:
            end += 1
        elif num > k:
            start += 1
    lst.sort(key=lambda x:(x[0],x[1]))
    answer = [lst[0][1],lst[0][2]]
    return answer