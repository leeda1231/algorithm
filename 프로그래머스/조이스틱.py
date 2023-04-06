def solution(name):
    answer = 0
    lst = []
    for x in name:
        num = ord(x)-65
        if num > 13:
            num = 26 - num
        lst.append(num)
    n = len(lst)
    move = n - 1
    for i in range(n):
        next = i + 1
        while next < n and lst[next] == 0:
            next += 1
        move = min(move, 2*i + n - next, i + 2*(n-next))
            
    answer = sum(lst) + move
    return answer