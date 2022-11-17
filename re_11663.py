n,m = map(int,input().split())
points = list(map(int,input().split()))
points.sort()

def binary_search(num):
    start = 0
    end = n - 1
    if num > points[end]:
        return n + 1
    if num < points[start]:
        return 0
    while start < end:
        mid = (start + end) // 2
        if num == points[mid]:
            return mid
        if num > points[mid]:
            start = mid + 1
        if num < points[mid]:
            end = mid - 1
    return start

for _ in range(m):
    s,e = map(int,input().split())
    print(binary_search(e),binary_search(s))