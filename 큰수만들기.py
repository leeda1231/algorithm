def solution(number, k):
    answer = ''
    num_lst = list(map(int,number))
    n = len(number) - k
    start = 0
    end = k
    while n > 0:
        # 정지조건 start = end?
        if start == end:
            answer += ''.join(map(str,num_lst[start:]))
            break
        max_val = 0
        new_start = start + 1
        for i in range(start,end+1):
            if num_lst[i] == 9:
                max_val = 9
                new_start = i+1
                break
            elif num_lst[i] > max_val:
                max_val = num_lst[i]
                new_start = i+1
        start = new_start
        end += 1
        answer += str(max_val)
        n -= 1
                
    return answer