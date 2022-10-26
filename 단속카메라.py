def solution(routes):
    answer = 1
    routes.sort(key = lambda x: (x[0],x[1]))
    start = routes[0][0]
    end = routes[0][1]
    for s,e in routes:
        if s > end:
            answer += 1
            start = s
            end = e
        if end > e:
            end = e
            
    return answer