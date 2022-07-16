n = int(input())
lst = list(map(int,input().split()))
lst_cal_num = list(map(int,input().split()))

maxv = -1e10
minv = 1e10

def dfs(d,result):
    global maxv,minv
    if d == n:
        maxv = max(maxv,result)
        minv = min(minv,result)
        return

    for i in range(4):
        if lst_cal_num[i] == 0:
            continue
        lst_cal_num[i] -= 1

        if i == 0:
            dfs(d+1,result+lst[d])
        elif i == 1:
            dfs(d+1, result-lst[d])
        elif i == 2:
            dfs(d+1, result*lst[d])
        elif i == 3:
            dfs(d+1, int(result/lst[d]))
        
        lst_cal_num[i] += 1

dfs(1,lst[0])
print(maxv)
print(minv)