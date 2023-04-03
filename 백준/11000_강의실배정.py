import heapq
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    s,t = map(int,input().split())
    lst.append((s,t))

lst.sort()
q = []
heapq.heappush(q, lst[0][1])

for i in range(1,n):
    # 현재 강의 시작시간이 (2,4)
    # 이전 강의들 중 가장 빠르게 끝난 시간보다 (1,3)
    # 작다면
    if lst[i][0] < q[0]:
        # 강의실 개설
        heapq.heappush(q,lst[i][1])
    # 아니면 이전: (1,3) / 현재: (3,5)
    else:
        # 이전 강의실 쓰고 현재 강의시간 큐에 추가
        heapq.heappop(q)
        heapq.heappush(q,lst[i][1])
        
print(len(q))
