n = int(input())

s = list(map(int,input().split()))

line = []
for i in range(n):
    line.insert(s[i],i+1)

print(*line[::-1])
