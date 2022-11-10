s = int(input())
'''
start = 0
end = 2 * s

def binary_search(start,end):
    while start <= end:
        mid = (start + end) // 2
        total = mid * (1+mid) // 2
        if total == s:
            break
        if total > s:
            end = mid - 1
        else:
            start = mid + 1
    return mid

print(binary_search(start,end))

'''
n = 1
total = 0
while 1:
    total += n
    if total == s:
        break
    elif total > s:
        n -= 1
        break
    n += 1
print(n)
