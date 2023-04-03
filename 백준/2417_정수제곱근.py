n = int(input())

def squareRoot(n):
    start = 0
    end = n
    while start <= end:
        mid = (start+end) // 2
        if n == mid*mid:
            return mid
        if n < mid*mid:
            end = mid - 1
        else:
            start = mid + 1
    return start

print(squareRoot(n))