from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    x = int(input())
    lst.append(x)
lst.sort()
a = round(sum(lst)/n)
b = lst[n//2]
c_dic = Counter(lst)
c_lst = c_dic.most_common(2)
if len(c_lst) > 1 and c_lst[0][1] == c_lst[1][1]:
    c = c_lst[1][0]
else:
    c = c_lst[0][0]
# m = max(c_dic.values())
# c_lst = [k for k,v in c_dic.items() if v == m]
# if len(c_lst) > 1:
#     c_lst.sort()
#     c = c_lst[1]
# else:
#     c = c_lst[0]
d = lst[-1] - lst[0]
print(a)
print(b)
print(c)
print(d)