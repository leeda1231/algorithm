# 절단기 높이 binary search
# key: 필요한 나무
def bi(N,key):
    start = 0
    end = N
    tree = 0
    while start <= end:
        mid = (start+end) // 2
        tree = 0
        for l in lst:
            if l > mid:
                tree += l-mid
        if tree == key:
            end = mid
            break
        # 잘라진 나무 > 필요한 나무 => 덜 필요해 => 높이 더 높게
        if tree >= key:
            start = mid + 1
        # 잘라진 나무 < 필요한 나무 => 더 필요해 => 높이 더 낮게
        else:
            end = mid - 1

    return end

n,m = map(int,input().split())
lst = list(map(int,input().split()))
print(bi(max(lst)-1,m))


# 시간초과 - 구현
# n,m = map(int,input().split())
# lst = list(map(int,input().split()))
# h = max(lst) - 1
# while 1:
#     tree = 0
#     for l in lst:
#         if l-h <= 0:
#             pass
#         else:
#             tree += l-h
#     if tree >= m:
#         break
#     h -= 1
# print(h)

