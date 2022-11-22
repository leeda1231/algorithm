from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
cnt = 0
for _ in range(n):
    command = input().strip()
    if command == 'pop':
        if cnt > 0:
            x = q.pop()
            print(x)
            cnt -= 1
        else:
            print(-1)
    elif command == 'size':
        print(cnt)
    elif command == 'empty':
        if cnt > 0:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if cnt > 0:
            print(q[-1])
        else:
            print(-1)
    else:
        x = int(command.split()[1])
        q.append(x)
        cnt += 1