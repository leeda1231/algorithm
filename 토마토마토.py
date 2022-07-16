import sys
from collections import deque
queue = deque()

#TO~TO~ 토~ 토마토마토 초기화
A, B = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(B)]
#print(array)

#dx[0],dy[0] : 상향 이동 등
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#가장 가까이 있는 익은 토마토위치 파악
for i in range(B):
  for j in range(A):
    if array[i][j] == 1:
      queue.append([i,j])

#토마토마토 익는중
while queue :
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      #if nx >=0 and nx < B and ny >= 0 and ny < A and array[nx][ny] == 0:
      if 0<= nx < B and 0<= ny <A and array[nx][ny] == 0:
        array[nx][ny] = array[x][y] + 1
        queue.append([nx, ny]) 

result = 0
for i in range(B):
  for j in range(A):
    if result < array[i][j]:
      result = array[i][j]
    if array[i][j] == 0:
      print(-1)
      exit()
        
#결과
print(result-1)