# 2
n = int(input())
cards = [0]* 20000001
lst = list(map(int,input().split()))
for l in lst:
    cards[l+10000000] = 1
m = int(input())
nums = list(map(int,input().split()))
for num in nums:
    if cards[num+10000000] == 1:
        print(1,end=' ')
    else:
        print(0,end=' ')

# 1
n = int(input())
cards = list(map(int,input().split()))
cards.sort()
m = int(input())
nums = list(map(int,input().split()))

def binary_search(cards,n):
    start = 0
    end = len(cards) - 1
    if n > cards[end] or n < cards[start]:
        return 0
    while start <= end:
        mid = (start + end) // 2
        if n == cards[mid]:
            return 1
        elif n < cards[mid]:
            end = mid - 1
        elif n > cards[mid]:
            start = mid + 1
    return 0

for i in range(m):
    x = binary_search(cards,nums[i])
    print(x, end=" ")