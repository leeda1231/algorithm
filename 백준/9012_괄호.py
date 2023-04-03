T = int(input())
for tc in range(T):
    data = list(input())
    lst = []
    for a in data:
        if a == '(':
            lst.append(a)
        elif a == ')':
            if len(lst) == 0:
                lst.append(')')
                break
            else:
                lst.pop()

    if len(lst) > 0:
        print('NO')
    else:
        print('YES')