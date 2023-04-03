n = int(input())
requests = list(map(int,input().split()))
requests.sort()
amount = int(input())

def binary_search(requests):
    start = requests[0]
    end = requests[-1]
    while start <= end:
        mid = (start+end) // 2
        total = 0
        for request in requests:
            if mid > request:
                total += request
            else:
                total += mid
        if total == amount:
            return min(requests[-1],mid)
        if total < amount:
            start = mid + 1
        elif total > amount:
            end = mid - 1
    return min(requests[-1],end)


if sum(requests) <= amount:
    print(requests[-1])
elif requests[0] * n > amount:
    print(amount//n)
else:
    print(binary_search(requests))