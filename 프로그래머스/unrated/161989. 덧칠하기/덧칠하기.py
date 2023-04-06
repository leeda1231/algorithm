def solution(n, m, section):
    answer = 0
    start = 1
    end = 0
    for s in section:
        if s <= end:
            continue
        start = s
        end = s + m - 1
        answer += 1
    return answer