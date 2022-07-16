n = int(input())
lst = list(map(int,input().split()))
min_val = int(1e6)
max_val = int(-1e6)
for num in lst:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print(min_val, max_val)