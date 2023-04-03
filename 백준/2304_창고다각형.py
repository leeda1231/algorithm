n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))

# 아이디어: 양옆에서 자신보다 큰 게 나올 때까지 높이 유지하며 더하기
lst.sort() 
maxV = 0
for i in range(n):
    if maxV < lst[i][1]:
        maxV = lst[i][1]
        idx = i

wid = 0
# 왼쪽
h = lst[0][1]
for i in range(idx):
    wid += (lst[i+1][0] - lst[i][0]) * h
    if h < lst[i+1][1]:
        h = lst[i+1][1]
    
# 가운데
wid += maxV

# 오른쪽
h = lst[-1][1]
for i in range(1,n-idx):
    wid += (lst[-i][0] - lst[-(i+1)][0]) * h
    if h < lst[-(i+1)][1]:
        h = lst[-(i+1)][1]

print(wid)

