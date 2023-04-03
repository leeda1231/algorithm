class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,value):
        self.items.append(value)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return "IndexError"

import sys
input = sys.stdin.readline
k = int(input().rstrip())
s = Stack()
total = 0
for _ in range(k):
    n = int(input().rstrip())
    if n == 0:
        x = s.pop()
        total -= x
    else:
        s.push(n)
        total += n

print(total)