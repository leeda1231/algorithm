
def check(lst):
    k = len(lst)
    print(lst[:k//2])
    print(lst[k//2:])
    if sum(lst[:k//2]) == sum(lst[k//2:]):
        return 1
    return 0

lst = (1,4,3,1,4)
print(check(lst))