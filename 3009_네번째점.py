lst_x = []
lst_y = []
for _ in range(3):
    x,y = map(int,input().split())
    lst_x.append(x)
    lst_y.append(y)
lst_x.sort()
lst_y.sort()
if lst_x[0] == lst_x[1]:
    ans_x = lst_x[2]
else:
    ans_x = lst_x[0]
if lst_y[0] == lst_y[1]:
    ans_y = lst_y[2]
else:
    ans_y = lst_y[0]

print(ans_x,ans_y)