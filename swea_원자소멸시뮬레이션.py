#2 수학 (시간줄어듬)
def meet(i,j):
    a = lst[i]
    b = lst[j]
    # dx >= 0
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    # 상하
    if dx == 0:
        if a[2] == 0 and b[2] == 1:
            out.append([dy,i,j])
    # 좌우
    elif dy == 0:
        if a[2] == 3 and b[2] == 2:
            out.append([dx,i,j])
    # 직각
    elif dx == dy:
        if a[2] == 0 and b[2] == 2 or a[2] == 3 and b[2] == 1:
            out.append([2*dx,i,j])
    elif dx == -dy:
        if a[2] == 3 and b[2] == 0 or a[2] == 1 and b[2] == 2:
            out.append([2*dx,i,j])


def emit(out):
    ans = 0
    v = [0] * n
    out.sort()
    for d,i,j in out:
        if v[i] == 0 and (v[j] == 0 or v[j] == d):
            v[i] = d
            ans += lst[i][3]
        if v[j] == 0 and (v[i] == 0 or v[i] == d):
            v[j] = d
            ans += lst[j][3]
    return ans

T = int(input())
for tc in range(T):
    n = int(input())
    lst = []
    out = []
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    lst.sort()
    for i in range(n-1):
        for j in range(i+1,n):
            meet(i,j)
    print(f'#{tc+1} {emit(out)}')


#1 시뮬
from collections import defaultdict

dir = {0:(0,1),1:(0,-1),2:(-1,0),3:(1,0)}

def move(dic):
    new_dic = defaultdict(list)
    for k,v in dic.items():
        if v:
            x,y = k
            d,e = v[0]
            nx = x + 0.5*dir[d][0]
            ny = y + 0.5*dir[d][1]
            new_dic[(nx,ny)].append((d,e))
    return new_dic

def emit(dic):
    global ans
    for k,v in dic.items():
        if len(v) > 1:
            ans += sum(map(lambda x:x[1],v))
            dic[k] = []
    return dic

T = int(input())
for tc in range(T):
    n = int(input())
    dic = defaultdict(list)
    ans = 0
    for _ in range(n):
        x,y,d,e = map(int,input().split())
        dic[(x,y)].append((d,e))
    for _ in range(4000):
        dic = move(dic)
        dic = emit(dic)

    print(f'#{tc+1} {ans}')