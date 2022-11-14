n,m = map(int,input().split())
title = dict()
title_lst = [0]
for _ in range(n):
    name,num = input().split()
    if title_lst[-1] != int(num):
        title[int(num)] = name
        title_lst.append(int(num))
if len(title_lst) != 1:
    title[0] = title[title_lst[1]]
powers = [int(input()) for _ in range(m)]

def binary_search(n):
    start = 0
    end = len(title_lst)
    while start <= end:
        mid = (start + end) // 2
        if n == title_lst[mid]:
            return mid
        if n < title_lst[mid]:
            end = mid - 1
        elif n > title_lst[mid]:
            start = mid + 1
    return start

for power in powers:
    print(title[title_lst[binary_search(power)]])