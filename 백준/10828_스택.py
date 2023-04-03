class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return -1
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1
    
    def __len__(self):
        return len(self.items)

import sys
input = sys.stdin.readline
n = int(input())
s = Stack()
for _ in range(n):
    command = input().strip()
    if command == 'pop':
        print(s.pop())
    elif command == 'size':
        print(len(s))
    elif command == 'empty':
        if len(s):
            print(0)
        else:
            print(1)
    elif command == 'top':
        print(s.top())
    else:
        s.push(int(command.split()[1]))


'''
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
'''