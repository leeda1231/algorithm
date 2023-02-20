#1
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