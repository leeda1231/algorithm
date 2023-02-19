n = int(input())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append([x,y,1])

for i in range(n-1):
    for j in range(i+1,n):
        x1,y1,z1 = lst[i]
        x2,y2,z2 = lst[j]
        if x1>x2 and y1>y2:
            lst[j][2] += 1
        elif x1<x2 and y1<y2:
            lst[i][2] += 1

print(*[l[2] for l in lst])