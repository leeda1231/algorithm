import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

x, y = p, q

print(x, y)

'''
0.15초: 반복문 쓰면 시간초과

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

x, y = p, q
dx, dy = 1, 1

for _ in range(t):
    x += dx
    y += dy

    if 0 < x < w and 0 < y < h:
        pass

    # 점
    elif x == w and y == h:
        dx, dy = -dx, -dy
        
    # 양 옆은 좌우만 바뀐다.
    elif x == 0 or x == w:
        dx = -dx

    # 위아래
    elif y == 0 or y == h:
        dy = -dy

print(x, y)
'''