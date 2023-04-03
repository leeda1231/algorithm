#2
n = int(input())
lst = list(map(int,input().split()))
max_val = max(lst)
total = 0
for i in range(n):
    total += lst[i]/max_val*100
print(total/n)

#1
n=int(input())
x=list(map(int,input().split()))
print(sum(x)*100/(n*max(x)))