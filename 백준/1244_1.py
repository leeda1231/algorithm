n = int(input()) # 스위치 개수
lst = list(map(int,input().split())) # 인덱스 주의 - 1
stu = int(input()) # 학생 수

for _ in range(stu):
    a, s = map(int,input().split())
    # 남
    if a == 1:
        i = 1
        while s*i <= n:
            lst[s*i-1] = (lst[s*i-1]+1)%2
            i += 1
    # 여
    elif a == 2:
        i = 0
        while s-i-1 >= 0 and s+i-1 < n:
            if lst[s-i-1] == lst[s+i-1]: # 좌우대칭
                lst[s-i-1] = lst[s+i-1] = (lst[s-i-1]+1)%2
                i += 1
            else:
                break

for j in range(0,n,20): # j = 0, 20, 40 ...
    print(*lst[j:j+20])