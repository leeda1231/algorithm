def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr)+1)//2
    l = arr[:mid]
    r = arr[mid:]
    l_ = merge_sort(l)
    r_ = merge_sort(r)
    return merge(l_,r_)


def merge(l,r):
    i,j = 0,0
    sorted_arr = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            ans.append(l[i])
            sorted_arr.append(l[i])
            i += 1
        else:
            ans.append(r[j])
            sorted_arr.append(r[j])
            j += 1
    while i < len(l):
        ans.append(l[i])
        sorted_arr.append(l[i])
        i += 1
    while j < len(r):
        ans.append(r[j])
        sorted_arr.append(r[j])
        j += 1
    return sorted_arr



n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = []
merge_sort(arr)
if k > len(ans):
    print(-1)
else:
    print(ans[k-1])