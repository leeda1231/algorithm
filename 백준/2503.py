from itertools import permutations

n = int(input())
lst =  list(permutations([i for i in range(1,10)],3))
for _ in range(n):
    num, s, b = map(int,input().split())