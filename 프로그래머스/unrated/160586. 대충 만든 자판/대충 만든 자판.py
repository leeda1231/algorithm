from collections import defaultdict

def solution(keymap, targets):
    answer = []
    key = defaultdict(int)
    for k in keymap:
        for i in range(len(k)):
            if key[k[i]] == 0:
                key[k[i]] = i+1
            elif key[k[i]] > i+1:
                key[k[i]] = i+1
    for target in targets:
        cnt = 0
        for t in target:
            if key[t] == 0:
                answer.append(-1)
                break
            cnt += key[t]
        else:
            answer.append(cnt)
    return answer