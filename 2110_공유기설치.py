n,c = map(int,input().split())
lst = []
for _ in range(n):
    x = int(input())
    lst.append(x)
lst.sort()

# 공유기의 설치 길이를 움직이자
end = lst[-1] - lst[0]
start = 1
ans = 0

# 이분 탐색 
def binary(lst, start, end):
    global ans
    while start <= end:
        mid = (start+end) // 2
        tmp = lst[0]
        cnt = 1

        for i in range(1,len(lst)):
            # gap이상(mid)
            if lst[i] >= tmp + mid:
                cnt += 1
                tmp = lst[i]
        
        # c개 이상
        if cnt >= c:
            start = mid + 1
            ans = mid
        
        else:
            end = mid - 1

binary(lst,start,end)
print(ans)
