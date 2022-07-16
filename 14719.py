h,w = map(int,input().split())
block = list(map(int,input().split()))
max_l = block[0]
max_r = block[0]
mid_v = block[0]
min_v = block[0]
block = block[1:]
q = []

ans = 0
for b in block:
    if b >= max_v:
        ans += len(q) * b - sum(q)
        q = []
        max_v = b
        mid_v = b
        min_v = b
    elif b < max_v:
        q.append(b)
    
print(ans)

# tmp = 0
# flag = 0
# for b in block:
#     if b < max_val:
#         tmp += max_val - b
#     elif b == max_val:
#         flag = 1
#     else:
#         flag = 1
#         max_val = b

# ans = 0
# if flag == 0 or flag == 1:
#     print(0)
# else:
#     print(ans)