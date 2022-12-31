lst_x = []
lst_y = []
for _ in range(3):
    x,y = map(int,input().split())
    lst_x.append(x)
    lst_y.append(y)
if lst_x[0] == lst_x[1]:
    ans_x = lst_x[2]
elif lst_x[0] == lst_x[2]:
    ans_x = lst_x[1]
elif lst_x[1] == lst_x[2]:
    ans_x = lst_x[0]
if lst_y[0] == lst_y[1]:
    ans_y = lst_y[2]
elif lst_y[0] == lst_y[2]:
    ans_y = lst_y[1]
elif lst_y[1] == lst_y[2]:
    ans_y = lst_y[0]

print(ans_x,ans_y)