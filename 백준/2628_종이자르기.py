# # w: 가로, l: 세로
# w , l = map(int,input().split())
# N = int(input())
# lst_w = [0,w] # 가로 리스트
# lst_l = [0,l] # 세로 리스트

# for i in range(N):
#     a, b = map(int,input().split())
#     # 가로로 자르는 점선(세로)
#     if a == 0:
#         lst_l.append(b) # 세로 리스트에 추가
#     # 세로로 자르는 점선(가로)
#     else:
#         lst_w.append(b) # 가로 리스트에 추가

# lst_w.sort()
# lst_l.sort()

# max_w = 0
# max_l = 0
# # [0,4,10] => [4,6]
# for i in range(len(lst_w)-1):
#     if lst_w[i+1]-lst_w[i] > max_w:
#         max_w = lst_w[i+1]-lst_w[i]
# # [0,2,3,8] => [2,1,5]
# for i in range(len(lst_l)-1):
#     if lst_l[i+1]-lst_l[i] > max_l:
#         max_l = lst_l[i+1]-lst_l[i]

# print(max_w*max_l)

w, l = map(int,input().split())
n = int(input())
lst_r = [0] # 행
lst_c = [0] # 열
for _ in range(n):
    a, b = map(int,input().split())
    # 가로로 자름
    if a == 0:
        lst_r += [b]
    # 세로로 자름
    else:
        lst_c += [b]

lst_r.sort()
lst_r += [l]
lst_c.sort()
lst_c += [w]

max_x = 0
max_y = 0
for i in range(len(lst_r)-1):
    x = lst_r[i+1] - lst_r[i]
    if x > max_x:
        max_x = x

for i in range(len(lst_c)-1):
    y = lst_c[i+1] - lst_c[i]
    if y > max_y:
        max_y = y

print(max_x * max_y)

