n = int(input())
cnt = 0
x = 666
while 1:
    s = str(x)
    if '666' in s:
        cnt += 1
    if cnt == n:
        print(x)
        break
    x += 1