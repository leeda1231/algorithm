# 완탐

# T = int(input())
# for _ in range(T):
#     lst = list(map(int,input().split()))
#     lst.sort(reverse=True)
#     print(lst[2])

# 카운트 정렬

T = int(input())
for _ in range(T):
    lst = list(map(int,input().split()))
    cnt = [0] * 1001
    for num in lst:
        cnt[num] += 1
    i = 1000
    val = 0
    while val < 3:
        if cnt[i] == 1:
            val += 1
        i -= 1
    print(i+1)