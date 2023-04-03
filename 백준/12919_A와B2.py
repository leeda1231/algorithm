s = input()
t = input()

# https://cseella.tistory.com/130

def dfs(x):
    global s, ans
    if len(x) == len(s):
        if x == s:
            ans = 1
        return
    if x[-1] == 'A':
        dfs(x[:-1])
    if x[0] == 'B':
        tmp = x[::-1]
        dfs(tmp[:-1])


# def dfs(x):
#     global t, ans
#     if len(x) == len(t):
#         if x == t:
#             ans = 1
#         else:
#             ans = 0
#         return
#     tmp = x + 'A'
#     if tmp in t:
#         dfs(tmp)
#     elif tmp[::-1] in t:
#         dfs(tmp)
#     else:
#         tmp = x + 'B'
#         tmp = tmp[::-1]
#         if tmp in t:
#             dfs(tmp)
#         elif tmp[::-1] in t:
#             dfs(tmp)
#         else:
#             ans = 0
#             return

ans = 0
dfs(t)
print(ans)