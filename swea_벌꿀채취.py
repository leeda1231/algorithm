#2
def honey(x,y,total,profit):
    global max_val
    if total > c:
        return
    if profit > max_val:
        max_val = profit
    if y < j+m:
        honey(x,y+1,total,profit)
        honey(x,y+1,total+arr[x][y],profit+arr[x][y]**2)


T = int(input())
for tc in range(T):
    n,m,c = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_lst = [0]*n
    for i in range(n):
        max_val = 0
        for j in range(n-m+1):
            honey(i,j,0,0)
        max_lst[i] = max_val
    max_lst.sort(reverse=True)
    ans = max_lst[0] + max_lst[1]
    print(f'#{tc+1} {ans}')



#1
from itertools import combinations

T = int(input())
for tc in range(T):
    n,m,c = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    new_arr = [[0]*(n-m+1) for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            if sum(arr[i][j:j+m]) <= c:
                for k in range(m):
                    new_arr[i][j] += arr[i][j+k]**2
            else:
                lst = arr[i][j:j+m]
                max_val = 0
                for l in range(m):
                    for x in combinations(lst,l):
                        tmp = 0
                        if sum(x) <= c:
                            for xx in x:
                                tmp += xx**2
                            if tmp > max_val:
                                max_val = tmp
                new_arr[i][j] += max_val

    # 다른 행에서 고를 경우
    max_lst = []
    for i in range(n):
        max_lst.append(max(new_arr[i]))
    max_lst.sort(reverse=True)
    ans = max_lst[0] + max_lst[1]
    print(f'#{tc+1} {ans}')
