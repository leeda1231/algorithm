def solution(dartResult):
    lst_num = []
    flag = 0 # 숫자가 10일 경우 구분 위해
    for i in dartResult:
        if i.isdecimal():
            if flag == 1:
                lst_num[-1] = 10
            else:
                flag = 1
                lst_num.append(int(i))
        elif i.isalpha():
            flag = 0
            if i == 'D':
                lst_num[-1] **= 2
            elif i == 'T':
                lst_num[-1] **= 3
            else:
                pass
        elif i == '*':
            flag = 0
            lst_num[-1] *= 2
            if len(lst_num) != 1:
                lst_num[-2] *= 2
        elif i == '#':
            flag = 0
            lst_num[-1] *= -1
    
    answer = sum(lst_num)
    return answer