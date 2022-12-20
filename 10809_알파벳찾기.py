word = input()
a = 97
ans = [-1] * 26
for i in range(len(word)):
    if ans[ord(word[i])-97] == -1:
        ans[ord(word[i])-97] = i

print(*ans)