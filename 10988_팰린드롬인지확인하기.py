s = input()
start = 0
end = len(s) - 1
while start <= end:
    if s[start] != s[end]:
        print(0)
        break
    start += 1
    end -= 1
else:
    print(1)