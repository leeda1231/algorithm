from collections import Counter

T = int(input())
for _ in range(T):
    tc,n = input().split()
    lst = list(input().split())
    c = Counter(lst)
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    ans = []
    for num in nums:
        ans += [num]*c[num]
    print(tc)
    print(' '.join(ans))