import sys
sys.setrecursionlimit(100000)

T = int(input())

def dfs(i):
    global cnt
    v[i] = 1
    cycles.append(i)
    if v[students[i]] == 1:
        if students[i] in cycles:
            cnt -= len(cycles[cycles.index(students[i]):])
        return
    dfs(students[i])



for _ in range(T):
    n = int(input())
    students = [0] + list(map(int,input().split()))
    v = [0] * (n+1)
    cnt = n
    for i in range(1,n+1):
        if v[i] == 0:
            cycles = []
            dfs(i)
    print(cnt)