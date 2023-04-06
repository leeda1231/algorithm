from collections import defaultdict

def solution(survey, choices):
    answer = ''
    p = defaultdict(int)
    n = len(survey)
    for i in range(n):
        if choices[i] > 4:
            p[survey[i][1]] += choices[i] - 4
        else:
            p[survey[i][0]] += 4 - choices[i]
    for x,y in [("R","T"),("C","F"),("J","M"),("A","N")]:
        if p[x] < p[y]:
            answer += y
        else:
            answer += x
    return answer