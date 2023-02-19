def merge_sort(arr):
    # 크기가 1이하면 반환
    if len(arr) <= 1:
        return arr
    # 리스트 2분할
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    #2분할한 리스트 각각 merge 진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_,right_)

def merge(left,right):
    i,j = 0,0
    sorted_arr = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr += left[i:]
    sorted_arr += right[j:]
    return sorted_arr

arr = [4,5,1,3,2]
print(merge_sort(arr))