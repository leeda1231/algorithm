lst = [-1] * 26
# a - 97 = 0
s = input()
for i in range(len(s)):
    if lst[ord(s[i])-97] == -1:
        lst[ord(s[i])-97] = i
print(*lst)