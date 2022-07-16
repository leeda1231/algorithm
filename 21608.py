from collections import defaultdict

n = int(input())
dic = defaultdict(list) # Keyerror 방지
arr = [[0]*n for _ in range(n)]
ans = 0

for q in range(n*n):
    a,b,c,d,e = map(int,input().split())
    dic[a] = [b,c,d,e]
    

    like_max = 0
    empty_max = 0
    for i in range(n):  
        for j in range(n):
            
            if arr[i][j] == 0:
                like = 0
                empty = 0
                for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx = i + dx
                    ny = j + dy
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] in dic[a]:
                            like += 1
                        if arr[nx][ny] == 0:
                            empty += 1

                #  1                   2 (# 3 2에서 등호 안쓰면 됨)
                if like_max < like or (like_max == like and empty_max < empty):
                    like_max = like
                    empty_max = empty
                    x = i
                    y = j

    # 마지막 남은 자리가 안 채워진다면(like=0, empty=0이어서)
    if q == n*n-1:
        for ii in range(n):
            for jj in range(n):
                if arr[ii][jj] == 0:
                    arr[ii][jj] = a                

    else:
        arr[x][y] = a

# 다 채워지면 좋아하는 사람 늘어나서 한 번 더 돌려줘야 함.   
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx = i + dx
            ny = j + dy
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] in dic[arr[i][j]]:
                cnt += 1
        
        if cnt == 0:
            s = 0
        elif cnt == 1:
            s = 1
        elif cnt == 2:
            s = 10
        elif cnt == 3:
            s = 100
        elif cnt == 4:
            s = 1000

        ans += s


print(ans)