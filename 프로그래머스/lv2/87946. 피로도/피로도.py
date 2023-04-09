from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    lst = [i for i in range(n)]
    for x in permutations(lst,n):
        cnt = 0
        tmp_k = k    
        for i in x:
            if tmp_k < dungeons[i][0]:
                break
            tmp_k -= dungeons[i][1]
            cnt += 1
        if cnt > answer:
            answer = cnt
    return answer