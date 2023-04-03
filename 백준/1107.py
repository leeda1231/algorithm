from itertools import product

n = int(input())
m = int(input())
if m != 0:
    brokenbuttons = set(map(int,input().split()))
    buttons = []
    for i in range(10):
        if i not in brokenbuttons:
            buttons.append(i)

def program(n,m):
    if n == 100:
        return 0
    if m == 0:
        return len(str(n))
    if m == 10:
        return abs(n-100)
    # 다 만들고 가까운 거 찾기
    l = len(str(n))
    min_val = 500000
    ans = 1000000
    # if 0 in buttons:
    #     for i in product(buttons, repeat=l):
    #         num = int(''.join(map(str,i)))
    #         # if num >= 500001:
    #         #     break
    #         if abs(num-n) < min_val:
    #             min_val = abs(num-n)
    #             ans = min_val + len(str(num))
    #     return ans

    # else:
    for i in product(buttons, repeat=l):
        num = int(''.join(map(str,i)))
        # if num >= 500001:
        #     break
        if abs(num-n) < min_val:
            min_val = abs(num-n)
            ans = min_val + len(str(num))
    if l != 6:
        for i in product(buttons, repeat=l+1):
            num = int(''.join(map(str,i)))
            # if num >= 500001:
            #     break
            if abs(num-n) < min_val:
                min_val = abs(num-n)
                ans = min_val + len(str(num))
            break
    if l != 1:
        for i in product(buttons, repeat=l-1):
            num = int(''.join(map(str,i)))
            # if num >= 500001:
            #     break
            if abs(num-n) < min_val:
                min_val = abs(num-n)
                ans = min_val + len(str(num))
    # print(min_val) 500000 344451 = 155549
    return ans

print(program(n,m))