from collections import deque

T = int(input())

def D(n):
    return (2*n)%10000

def S(n):
    if n == 0:
        return 9999
    return n-1

def L(n):
    a = n // 1000
    b = n * 10
    return b - 9999*a

def R(n):
    a = n // 10
    b = n % 10
    return 1000*b + a

def bfs(x,y):
    q = deque([[x,""]])
    v = [0] * 10000
    v[x] = 1
    while q:
        x,command = q.popleft()
        if x == y:
            print(command)
            break
        if v[D(x)] == 0:
            v[D(x)] = 1
            q.append([D(x),command+"D"])
        if v[S(x)] == 0:
            v[S(x)] = 1
            q.append([S(x),command+"S"])
        if v[L(x)] == 0:
            v[L(x)] = 1
            q.append([L(x),command+"L"])
        if v[R(x)] == 0:
            v[R(x)] = 1
            q.append([R(x),command+"R"])

for _ in range(T):
    a,b = map(int,input().split())
    bfs(a,b)

'''
# 이전 풀이
from collections import deque

T = int(input())

def D(n):
    return (2*n)%10000

def S(n):
    if n == 0:
        return 9999
    return n-1

def L(n):
    return n*10 - 9999*(n//1000)

def R(n):
    return n//10 + n%10*1000

def bfs(n,m):
    q = deque([[n,""]])
    visited = [0] * 10000
    visited[n] = 1
    while q:
        x = q.popleft()
        if x[0] == m:
            return x[1]
        if visited[D(x[0])] == 0:
            visited[D(x[0])] = 1
            q.append([D(x[0])] + [x[1]+'D'])
        if visited[S(x[0])] == 0:
            visited[S(x[0])] = 1
            q.append([S(x[0])] + [x[1]+'S'])
        if x[-1] != 'R' and visited[L(x[0])] == 0:
            visited[L(x[0])] = 1
            q.append([L(x[0])] + [x[1]+'L'])
        if x[-1] != 'L' and visited[R(x[0])] == 0:
            visited[R(x[0])] = 1
            q.append([R(x[0])] + [x[1]+'R'])

for _ in range(T):
    a,b = map(int,input().split())
    ans = bfs(a,b)
    print(ans)


# 메모리 초과
from collections import deque

T = int(input())

def D(n):
    return (2*n)%10000

def S(n):
    if n == 0:
        return 9999
    return n-1

def L(n):
    return n*10 - 9999*(n//1000)

def R(n):
    return n//10 + n%10*1000

def bfs(n,m):
    q = deque([[n]])
    while q:
        x = q.popleft()
        if x[0] == m:
            return x[1:]
        q.append([D(x[0])] + x[1:] + ['D'])
        q.append([S(x[0])] + x[1:] + ['S'])
        if x[-1] != 'R':
            q.append([L(x[0])] + x[1:] + ['L'])
        if x[-1] != 'L':
            q.append([R(x[0])] + x[1:] + ['R'])

for _ in range(T):
    a,b = map(int,input().split())
    ans = bfs(a,b)
    print(''.join(ans))
'''