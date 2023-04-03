lst = [int(input()) for _ in range(9)]
total = sum(lst)

for i in range(9):
    for j in range(i):
        if lst[i] + lst[j] == total - 100:
            x,y = lst[i], lst[j]

lst.remove(x)
lst.remove(y)
lst.sort()

for i in lst:
    print(i)

# lst = [int(input()) for _ in range(9)]
# lst_sum = sum(lst)

# a = 0
# b = 1

# while b < 9:
    
#     total = lst_sum - lst[a] - lst[b]
    
#     if total == 100:
#         aa = lst[a]
#         bb = lst[b]
#         break

#     elif b < 8 and a < b:
#         b += 1

#     elif b == 8:
#         a += 1
#         b = a+1

# lst.remove(aa)
# lst.remove(bb)
# lst.sort()
# for i in lst:
#     print(i)
