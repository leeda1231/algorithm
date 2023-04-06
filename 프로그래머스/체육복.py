def solution(n, lost, reserve):
    lost_set = set(lost)
    union = lost_set & set(reserve)
    answer = n - len(lost) + len(union)
    for x in union:
        reserve.remove(x)
        lost_set.remove(x)
    reserve.sort()
    for student in reserve:
        if student - 1 in lost_set:
            lost_set.remove(student-1)
            answer += 1
        elif student + 1 in lost_set:
            lost_set.remove(student+1)
            answer += 1
    return answer