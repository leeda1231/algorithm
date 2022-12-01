n = int(input())
s = input()
tmp = 'N'
cnt = 0
b = 0
for i in s:
    if i != tmp:
        cnt += 1
        tmp = i
        if tmp == 'B':
            b += 1

print(min(cnt,b+1,cnt-b+1))