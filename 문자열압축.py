def solution(s):
    answer = len(s)
    # 문자열 1개 단위 ~ len(s)-1 단위까지 잘라서 lst에 넣기
    n = 1
    while n < len(s):
        lst = []
        for idx in range(0,len(s),n):
            lst.append(s[idx:idx+n])
        tmp = lst[0]
        cnt = 1
        result = ''
        for i in range(1,len(lst)):
            if lst[i-1] == lst[i]:
                cnt += 1
                if i == len(lst)-1:
                    if cnt > 1:
                        result += str(cnt) + tmp
                    else:
                        result += tmp
            elif lst[i-1] != lst[i]:
                if cnt > 1:
                    result += str(cnt) + tmp
                else:
                    result += tmp
                cnt = 1
                tmp = lst[i]
                if i == len(lst) - 1:
                    result += tmp
        if len(result) < answer:
            answer = len(result)
        n += 1
        
            
    return answer