n = int(input())
lst = [i for i in range(1,n+1)]
while len(lst) > 1:
    tmp_lst = []
    for i in range(1,len(lst),2):
        tmp_lst.append(lst[i])
    lst = tmp_lst

print(lst[0])