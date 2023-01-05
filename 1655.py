import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    heapq.heappush(heap,x)
    print(heap)