cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
ans = len(s)
for c in cro:
    ans -= s.count(c)
print(ans)