#2
T = int(input())
for _ in range(T):
    n,s = input().split()
    n = int(n)
    ans = ''
    for i in range(len(s)):
        ans += s[i] * n
    print(ans)

#1
T = int(input())
for _ in range(T):
    x,word = input().split()
    for w in word:
        for _ in range(int(x)):
            print(w,end='')
    print()