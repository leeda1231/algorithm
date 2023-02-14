T = int(input())
for tc in range(T):
    a = list(input())
    b = list(input())
    flag = 0
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
            x = int(''.join(a),2)
            for j in range(len(b)):
                if b[j] == '0':
                    b[j] = '1'
                    y = int(''.join(b),3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '2'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '0'
                elif b[j] == '1':
                    b[j] = '0'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '2'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '1'
                else:
                    b[j] = '0'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '1'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '2'
            a[i] = '0'
        else:
            a[i] = '0'
            x = int(''.join(a), 2)
            for j in range(len(b)):
                if b[j] == '0':
                    b[j] = '1'
                    y = int(''.join(b),3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '2'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '0'
                elif b[j] == '1':
                    b[j] = '0'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '2'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '1'
                else:
                    b[j] = '0'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '1'
                    y = int(''.join(b), 3)
                    if x == y:
                        ans = x
                        flag = 1
                        break
                    b[j] = '2'
            a[i] = '1'
        if flag == 1:
            break
    print(f'#{tc+1}',ans)