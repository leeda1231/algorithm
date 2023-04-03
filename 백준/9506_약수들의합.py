while 1:
    n = int(input())
    if n == -1:
        break
    total = 0
    lst = []
    for i in range(1,n//2+1):
        if n % i == 0:
            total += i
            lst.append(i)
            if total > n:
                break
    if total == n:
        print(f'{n} = {" + ".join(map(str,lst))}')
    else:
        print(f'{n} is NOT perfect.')