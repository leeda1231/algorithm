n,k = map(int,input().split())
lst = list(map(int,input().split()))
belt = [[],[]]
belt[0] += lst[:n]
belt[1] += lst[n:]
robot = [[0]*n for _ in range(2)]

cnt = 0
step = 0

while cnt < k:
    # 회전(벨트, 로봇)
    pass