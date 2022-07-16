'''
# 인덱스 나중에 고친 것
lst = list(input())
N = len(lst)
cnt = 0
for i in range(N):
    if lst[i] == 'Y':
        cnt += 1
        for j in range(1,N//(i+1)+1):
            if lst[(i+1)*j-1] == 'Y':
                lst[(i+1)*j-1] = 'N'
            else:
                lst[(i+1)*j-1] = 'Y'

    if 'Y' not in lst:
        break
else:
    cnt = -1

print(cnt)
'''

# lst = ['N'] + list(input())
# N = len(lst)
# cnt = 0
# for i in range(1,N):
#     if lst[i] == 'Y':
#         cnt += 1
#         for j in range(1,(N-1)//i+1):
#             if lst[i*j] == 'Y':
#                 lst[i*j] = 'N'
#             else:
#                 lst[i*j] = 'Y'

#     if 'Y' not in lst:
#         break
# else:
#     cnt = -1

# print(cnt)

lst = ['N'] + list(input())
cnt = 0
i = 0

while 'Y' in lst:
    i += 1
    if lst[i] == 'Y':
        cnt += 1
        for j in range(i,len(lst),i):
            if lst[j] == 'Y':
                lst[j] = 'N'
            else:
                lst[j] = 'Y'

    if i == len(lst) + 1 and 'Y' in lst:
        cnt = -1
        break

print(cnt)