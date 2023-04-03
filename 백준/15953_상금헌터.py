# 상금 헌터

def prize_a(x):
    
    if x == 0:
        money = 0
    elif x == 1:
        money = 5000000
    elif x < 4:
        money = 3000000
    elif x < 7:
        money = 2000000
    elif x < 11:
        money = 500000
    elif x < 16:
        money = 300000
    elif x < 22:
        money = 100000
    else:
        money = 0
    
    return money

def prize_b(x):

    if x == 0:
        money = 0
    elif x == 1:
        money = 5120000
    elif x < 4:
        money = 2560000
    elif x < 8:
        money = 1280000
    elif x < 16:
        money = 640000
    elif x < 32:
        money = 320000
    else:
        money = 0
    
    return money

T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    print(prize_a(a) + prize_b(b))
