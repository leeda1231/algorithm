for tc in range(1,11):
    n = int(input())
    lst = list(input().split())
    m = int(input())
    command = list(input().split())
    cnt = 0
    i = 0
    while cnt < m:
        if command[i].isalpha():
            if command[i] == 'I':
                x = int(command[i + 1])
                y = int(command[i + 2])
                z = i + 3
                for j in range(x, x + y):
                    lst.insert(j, command[z])
                    z += 1
                i += y + 3
            elif command[i] == 'D':
                x = int(command[i+1])
                y = int(command[i+2])
                del lst[x:x+y]
                i += 3
            elif command[i] == 'A':
                y = int(command[i+1])
                for j in range(i+2,i+2+y):
                    lst.append(command[j])
                i += y + 2
        cnt += 1
    print(f'#{tc} {" ".join(lst[:10])}')