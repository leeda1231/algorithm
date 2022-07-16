# 오른쪽으로만 갈 수 있다.
# 이동 횟수가 4번 이상이라면, 모두 한 번씩 써야 한다. 
n, m = map(int,input().split())

# 이동 횟수가 4번 이상인 경우(그 중에서도 모두 한 번씩 써서 가능한 경우)
if n >= 3 and m >= 7:
    print(m-2)

# 가로로 1줄인 경우
elif n == 1:
    print(1) # print(n)을 썼더니 런타임 에러가 떴다. 

# 가로로 2줄인 경우
elif n == 2:
    if m < 3:
        print(1)
    elif m < 5:
        print(2)
    elif m < 7:
        print(3)
    else:            # m == 7 로 썼다가 틀렸었다. m >= 7 일때로 생각해줘야함. 
        print(4)

# 가로로 3줄인 경우
elif n == 3:
    if m < 5:
        print(m)
    # 이동횟수가 4번 이상인데 모두 한 번씩 쓰면 불가능.
    elif m == 5 or m == 6:
        print(4)

else:
    # 세로로 1~4줄인 경우
    if m < 5:
        print(m)

#세로로 5~6줄인 경우(이동횟수가 4번 이상인데 모두 한 번씩 쓰면 불가능)
    elif m == 5 or m == 6:
        print(4)


