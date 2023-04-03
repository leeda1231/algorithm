max_v = 0
x,y = 0,0
arr = [list(map(int,input().split())) for _ in range(9)]
for i in range(9):
    tmp_max = max(arr[i])
    if tmp_max > max_v:
        max_v = tmp_max
        x,y = i,arr[i].index(tmp_max)
print(max_v)
print(x+1,y+1)