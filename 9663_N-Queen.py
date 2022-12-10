n = int(input())
v = [0] * n # 인덱스: 행, 원소: 열
ans = 0

def dfs(x):
    global ans
    if x == n:
        ans += 1
        return
    for j in range(n):
        v[x] = j
        for i in range(x):
            # 세로 / 왼오대각선
            if v[x] == v[i] or abs(v[x]-v[i]) == (x-i):
                break
        else:
            dfs(x+1)

dfs(0)
print(ans)