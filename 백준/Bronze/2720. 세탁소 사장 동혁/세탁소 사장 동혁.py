T = int(input())
for _ in range(T):
    change = int(input())
    money = [25,10,5,1]
    cnt = [0,0,0,0]
    for i in range(4):
        if change >= money[i]:
            cnt[i] += change // money[i]
            change %= money[i]
    print(*cnt)