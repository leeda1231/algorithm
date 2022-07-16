'''
이동하는 인덱스
그에 따른 모래 이동
바깥에 나오는 모래 찾기
'''
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
# 왼 아래 오 위
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 시작점
x, y = n//2, n//2
# d = 0
# # 인덱스 이동
# for i in range(n):
#     nx = x + dx[d]
#     ny = y + dy[d]
#     d = (d + 1) // 4

d = -1
out = 0
while 0 <= x < n and 0 <= y < n:
    d += 1
    l = d // 2 + 1
    
    for _ in range(l):
        nx = x + dx[d % 4]
        ny = y + dy[d % 4]
        left = 0
        if ny == -1:
            break
        
        # 무엇인가 작업
        now = arr[nx][ny]
        # 7퍼
        for k in [1,-1]:
            nnx = nx + dx[(d+k)%4]
            nny = ny + dy[(d+k)%4]
            if 0 <= nnx < n and 0 <= nny < n:
                arr[nnx][nny] += int(now*0.07)
            else:
                out += int(now*0.07)
            left += int(now*0.07)
        # 2퍼
        for k in [1,-1]:
            nnx = nx + dx[(d+k)%4]*2
            nny = ny + dy[(d+k)%4]*2
            if 0 <= nnx < n and 0 <= nny < n:
                arr[nnx][nny] += int(now*0.02)
            else:
                out += int(now*0.02)
            left += int(now*0.02)

        # 1퍼
        for k in [1,-1]:
            nnx = x + dx[(d+k)%4]
            nny = y + dy[(d+k)%4]
            if 0 <= nnx < n and 0 <= nny < n:
                arr[nnx][nny] += int(now*0.01)
            else:
                out += int(now*0.01)
            left += int(now*0.01)

        # 10퍼
        for k in [1,-1]:
            nnx = x + dx[(d+k)%4]
            nny = y + dy[(d+k)%4]
            if 0 <= nnx < n and 0 <= nny < n:
                arr[nnx][nny] += int(now*0.01)
            else:
                out += int(now*0.01)
            left += int(now*0.01)


        # 마지막
        arr[nx][ny] - left = '알파'
        
        # 작업 끝
        x,y = nx, ny
        