n = int(input()) # 첫번째 수

max = 0 # 최대 개수

for x2 in range(1,n+1): # 세번째 수가 0이상의 정수가 되는 범위
    x3 = n - x2
    cnt = 0 
    lst = [n,x2,x3]

    while x3 >= 0: # x4, x5, x6 ... 음수 될 때까지
        x1 = x2
        x2 = x3
        x3 = x1 - x2
        cnt += 1
        lst.append(x3)
    
    if max < cnt:
        max = cnt
        ans = lst
        ans.pop() # 마지막 음수 삭제

print(len(ans))
print(*ans)
