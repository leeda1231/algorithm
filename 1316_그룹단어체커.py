n = int(input())
ans = 0
for _ in range(n):
    word = input()
    tmp = word[0]
    v = set()
    v.add(tmp)
    for w in word:
        if tmp != w:
           if w in v:
               break
           tmp = w
           v.add(w)
    else:
        ans += 1
print(ans)