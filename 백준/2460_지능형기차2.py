cnt = 0
max_val = 0
for _ in range(10):
    out, inn = map(int,input().split())
    cnt += inn - out
    if max_val < cnt:
        max_val = cnt

print(max_val)