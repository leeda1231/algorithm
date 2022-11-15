n,m = map(int,input().split())
points = list(map(int,input().split()))
points.sort()

def binary_search_start(num):
    start = 0
    end = n - 1
    if num < points[start]:
        return 0
    while start <= end:
        mid = (start + end) // 2
        if num == points[mid]:
            return mid
        if num > points[mid]:
            start = mid + 1
        if num < points[mid]:
            end = mid - 1
    return start - 1

def binary_search_end(num):
    start = 0
    end = n - 1
    if num > points[end]:
        return n
    while start <= end:
        mid = (start + end) // 2
        if num == points[mid]:
            return mid + 1
        if num > points[mid]:
            start = mid + 1
        if num < points[mid]:
            end = mid - 1
    return start - 1

for _ in range(m):
    s,e = map(int,input().split())
    print(binary_search_end(e) - binary_search_start(s))