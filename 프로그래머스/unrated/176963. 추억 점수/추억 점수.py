from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    y = defaultdict(int)
    for i in range(len(name)):
        y[name[i]] = yearning[i]
    for p in photo:
        cnt = 0
        for pp in p:
            cnt += y[pp]
        answer.append(cnt)
    return answer