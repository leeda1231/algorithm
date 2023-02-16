#1
n,m = map(int,input().split())
arr1 = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int,input().split())) for _ in range(n)]
arr3 = zip(arr1,arr2)
for a in arr3:
    for x,y in zip(*a):
        print(x+y,end=' ')
    print()

#2
arr4 = [[a+b for a,b in zip(x,y)] for x,y in zip(arr1,arr2)]
for b in arr4:
    print(*b)