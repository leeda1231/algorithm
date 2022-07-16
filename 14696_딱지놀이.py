N = int(input())

for _ in range(N):
    
    a, *lst_a = map(int,input().split())
    b, *lst_b = map(int,input().split())

    if lst_a.count(4) > lst_b.count(4):
        print('A')
    elif lst_a.count(4) < lst_b.count(4):
        print('B')

    elif lst_a.count(3) > lst_b.count(3):
        print('A')
    elif lst_a.count(3) < lst_b.count(3):
        print('B')

    elif lst_a.count(2) > lst_b.count(2):
        print('A')
    elif lst_a.count(2) < lst_b.count(2):
        print('B')

    elif lst_a.count(1) > lst_b.count(1):
        print('A')
    elif lst_a.count(1) < lst_b.count(1):
        print('B')

    else:
        print('D')