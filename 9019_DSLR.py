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



# 메모리초과
# from collections import deque

# T = int(input())

# def D(n):
#     return (2*n)%10000

# def S(n):
#     if n == 0:
#         return 9999
#     return n-1

# def L(n):
#     return n*10 - 9999*(n//1000)

# def R(n):
#     return n//10 + n%10*1000

# def bfs(n,m):
#     q = deque([[n]])
#     while q:
#         x = q.popleft()
#         if x[0] == m:
#             return x[1:]
#         q.append([D(x[0])] + x[1:] + ['D'])
#         q.append([S(x[0])] + x[1:] + ['S'])
#         if x[-1] != 'R':
#             q.append([L(x[0])] + x[1:] + ['L'])
#         if x[-1] != 'L':
#             q.append([R(x[0])] + x[1:] + ['R'])

# for _ in range(T):
#     a,b = map(int,input().split())
#     ans = bfs(a,b)
#     print(''.join(ans))