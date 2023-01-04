from collections import deque

n,k = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([0]*n)
ans = 0
while 1:
    ans += 1
    # 1
    belt.rotate()
    robot.rotate()
    robot[n-1] = 0
    # 2
    for i in range(n-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
    if robot[n-1] == 1:
        robot[n-1] = 0
    # 3
    if belt[0]:
        robot[0] = 1
        belt[0] -= 1
    # 4
    cnt = belt.count(0)
    if cnt >= k:
        print(ans)
        break