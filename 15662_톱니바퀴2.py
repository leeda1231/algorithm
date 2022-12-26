from collections import deque

T = int(input())

for i in range(1,T+1):
    globals()[f'g{i}'] = deque(map(int,input()))

rotate_lst = [0] * T

def move_r(n):
    if n == T:
        return
    if globals()[f'g{n}'][2] == globals()[f'g{n+1}'][-2]:
        return
    if rotate_lst[n-1] == 1:
        rotate_lst[n] = -1
    else:
        rotate_lst[n] = 1
    move_r(n+1)


def move_l(n):
    if n == 1:
        return
    
    if globals()[f'g{n-1}'][2] == globals()[f'g{n}'][-2]:
        return
    if rotate_lst[n-1] == 1:
        rotate_lst[n-2] = -1
    else:
        rotate_lst[n-2] = 1
    move_l(n-1)


k = int(input())
for _ in range(k):
    rotate_lst = [0] * T
    n,d = map(int,input().split())
    rotate_lst[n-1] = d
    move_r(n)
    move_l(n)
    for i in range(T):
        if rotate_lst[i] == 1:
            globals()[f'g{i+1}'].rotate()
        elif rotate_lst[i] == -1:
            globals()[f'g{i+1}'].rotate(-1)

ans = 0
for i in range(1,T+1):
    if globals()[f'g{i}'][0] == 1:
        ans += 1

print(ans)