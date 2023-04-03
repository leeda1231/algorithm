dir = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = list(input())
ans = 0
for w in word:
    for i in range(len(dir)):
        if w in dir[i]:
            ans += i+3
print(ans)