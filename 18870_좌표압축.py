import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
tmp_lst = sorted(list(set(lst)))
tmp_dic = {tmp_lst[i]:i for i in range(len(tmp_lst))}
for l in lst:
    print(tmp_dic[l],end=' ')