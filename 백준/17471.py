import itertools

n = int(input())
num = [0] + list(map(int,input().split()))
lst = [[]]
ans = -1
for i in range(1,n+1):
    n,*data = map(int,input().split())
    lst.append(data)

# 조합으로 구역 다 나누기 -> 되는 것들 중에 최소값 찾기
for i in range(2//n):
    data = list(itertools.combinations(lst,i))
print(data)