a,b,c = map(int,input().split())
s = set()
s.update([a,b,c])

def sol(s):
    global a,b,c
    if len(s) == 3:
        return max(s) * 100
    if len(s) == 1:
        return 10000 + a*1000
    # if len(s) == 2:
    if a == b or a == c:
        return 1000 + a * 100
    return  1000 + b * 100

print(sol(s))