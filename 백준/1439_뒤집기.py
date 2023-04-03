s = input()
first = s[0]
cnt = 0
for i in range(1,len(s)):
    last = s[i]
    if first != last:
        cnt += 1
    first = last
print(cnt//2 + cnt%2)