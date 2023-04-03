# n = int(input()) # 스위치 개수
# lst = list(map(int,input().split())) # 인덱스 주의. 이따가 - 1
# stu = int(input()) # 학생 수

# for _ in range(stu):
#     a, s = map(int,input().split())
#     # 남
#     if a == 1:
#         i = 1
#         while s*i <= n:
#             if lst[s*i - 1] == 0:
#                 lst[s*i - 1] = 1
#             else:
#                 lst[s*i - 1] = 0
#             i += 1
#     # 여
#     elif a == 2:
#         i = 0
#         while s-i-1 >= 0 and s+i-1 < n:
#             if lst[s-i-1] == lst[s+i-1]: # 좌우대칭
#                 if lst[s-i-1] == 0:
#                     lst[s-i-1] = lst[s+i-1] = 1
#                 else:
#                     lst[s-i-1] = lst[s+i-1] = 0
#                 i += 1
#             else:
#                 break

# for j in range(0,n,20): # j = 0, 20, 40 ...
#     print(*lst[j:j+20])

n = int(input())
lst = list(map(int,input().split())) # 인덱스 주의 -1
stu = int(input())
for _ in range(stu):
    a,s = map(int,input().split())
    # 남
    if a == 1:
        for i in range(s,n+1,s):
            if lst[i-1] == 0:
                lst[i-1] = 1
            else:
                lst[i-1] = 0
    # 여
    else:
        i = 0
        while s-1-i >= 0 and s-1+i < n:
            if lst[s-1-i] == lst[s-1+i]:
                if lst[s-1-i] == 0:
                    lst[s-1-i] = lst[s-1+i] = 1
                else:
                    lst[s-1-i] = lst[s-1+i] = 0
                i += 1
            else:
                break

for j in range(0,n,20):
    print(*lst[j:j+20])