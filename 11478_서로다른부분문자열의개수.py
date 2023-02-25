s = input()
n = len(s)
set_s = set()
for i in range(1,n+1):
    for j in range(0,n-i+1):
        set_s.add(s[j:j+i])
print(len(set_s))