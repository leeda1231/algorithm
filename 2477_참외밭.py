n = int(input())
lst = [list(map(int,input().split())) for _ in range(6)]
# print(lst)
w = 0 # 가장 긴 가로가 될 것
h = 0 # 가장 긴 세로가 될 것

for i in range(6):
    if lst[i][0] == 1 or lst[i][0] == 2: # 동,서
        if w < lst[i][1]:
            w = lst[i][1]  # 가장 큰 가로변
            w_idx = i  # 의 인덱스

    elif lst[i][0] == 3 or lst[i][0] == 4: # 남,북
        if h < lst[i][1]:
            h = lst[i][1]  # 가장 큰 세로변
            h_idx = i  # 의 인덱스

# 빼야 하는 작은 사각형
# 인덱스가 5로 가장 끝에 있을 경우 때문에           0 1 2 3 4 5
w_min = abs(lst[(w_idx+1)%6][1]-lst[w_idx-1][1])
h_min = abs(lst[(h_idx+1)%6][1]-lst[h_idx-1][1])

print(n*((w*h)-(w_min*h_min)))