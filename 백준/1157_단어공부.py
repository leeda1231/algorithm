word = input().upper()
lst = [0] * 26
# A - 65 = 0
for w in word:
    lst[ord(w)-65] += 1
n = max(lst)
ans = list(filter(lambda x:lst[x] == n, range(26)))
# ans2 = [x for x in range(26) if lst[x] == n]

if len(ans) > 1:
    print("?")
else:
    x = ans[0] + 65
    print(chr(x))