while 1:
    try:
        n, k = map(int,input().split())
        tmp = n # 안 쓴 도장 수

        while tmp//k > 0:
            n += tmp // k
            tmp = tmp // k + tmp % k

        print(n)
    except:
        break