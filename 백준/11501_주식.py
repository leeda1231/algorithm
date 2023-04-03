T = int(input())
for _ in range(T):
    n = int(input())
    stocks = list(map(int,input().split()))
    answer = 0
    max_val = stocks[-1]
    for i in range(n-2,-1,-1):
        if stocks[i] < max_val:
            answer += max_val - stocks[i]
        else:
            max_val = stocks[i]

    print(answer)