from collections import defaultdict

T = int(input())
for _ in range(T):
    W = input()
    n = len(W)
    K = int(input())
    min_ans = n+1
    max_ans = 0
    dic = defaultdict(list)
    for i in range(n):
        dic[W[i]].append(i)
    
    for value in dic.values():
        if len(value) < K:
            continue
        for d in range(0,len(value)-K+1):
            tmp = value[d+K-1] - value[d] + 1
            if tmp > max_ans:
                max_ans = tmp
            if tmp < min_ans:
                min_ans = tmp

    if min_ans == n+1 or max_ans == 0:
        print(-1)
    else:
        print(min_ans,max_ans)


        



        


