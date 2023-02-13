#2
pieces = [1,1,2,2,2,8]
lst = list(map(int,input().split()))
print(*[x-y for x,y in zip(pieces,lst)])

#1
lst = list(map(int,input().split()))
chess = [1,1,2,2,2,8]
for i in range(len(lst)):
    lst[i] = chess[i] - lst[i]
print(*lst)