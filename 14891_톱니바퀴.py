from collections import deque

g1 = deque(map(int,input()))
g2 = deque(map(int,input()))
g3 = deque(map(int,input()))
g4 = deque(map(int,input()))
rotate_lst = [0,0,0,0]

def rotate_r(q):
    q.appendleft(q.pop())
    return

def rotate_l(q):
    q.append(q.popleft())
    return

def move_r(n):
    if n == 4:
        return
    if n == 1:
        if g1[2] == g2[-2]:
            return
        if rotate_lst[0] == 1:
            rotate_lst[1] = -1
        else:
            rotate_lst[1] = 1
        move_r(n+1)
    elif n == 2:
        if g2[2] == g3[-2]:
            return
        if rotate_lst[1] == 1:
            rotate_lst[2] = -1
        else:
            rotate_lst[2] = 1
        move_r(n+1)
    elif n == 3:
        if g3[2] == g4[-2]:
            return
        if rotate_lst[2] == 1:
            rotate_lst[3] = -1
        else:
            rotate_lst[3] = 1
        move_r(n+1)


def move_l(n):
    if n == 1:
        return
    if n == 2:
        if g1[2] == g2[-2]:
            return
        if rotate_lst[1] == 1:
            rotate_lst[0] = -1
        else:
            rotate_lst[0] = 1
        move_l(n-1)
    elif n == 3:
        if g2[2] == g3[-2]:
            return
        if rotate_lst[2] == 1:
            rotate_lst[1] = -1
        else:
            rotate_lst[1] = 1
        move_l(n-1)
    elif n == 4:
        if g3[2] == g4[-2]:
            return
        if rotate_lst[3] == 1:
            rotate_lst[2] = -1
        else:
            rotate_lst[2] = 1
        move_l(n-1)


k = int(input())
for _ in range(k):
    rotate_lst = [0,0,0,0]
    n,d = map(int,input().split())
    rotate_lst[n-1] = d
    move_r(n)
    move_l(n)
    if rotate_lst[0] == 1:
        rotate_r(g1)
    elif rotate_lst[0] == -1:
        rotate_l(g1)
    if rotate_lst[1] == 1:
        rotate_r(g2)
    elif rotate_lst[1] == -1:
        rotate_l(g2)
    if rotate_lst[2] == 1:
        rotate_r(g3)
    elif rotate_lst[2] == -1:
        rotate_l(g3)
    if rotate_lst[3] == 1:
        rotate_r(g4)
    elif rotate_lst[3] == -1:
        rotate_l(g4)

ans = 0
if g1[0] == 1:
    ans += 1
if g2[0] == 1:
    ans += 2
if g3[0] == 1:
    ans += 4
if g4[0] == 1:
    ans += 8

print(ans)