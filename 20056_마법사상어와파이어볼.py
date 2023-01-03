n,m,k = map(int,input().split())
fireballs = []
for _ in range(m):
    r,c,m,s,d = map(int,input().split())
    fireballs.append((r-1,c-1,m,s,d))
dir = {0:(-1,0), 1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1)}

# 1
def move(fireballs):
    board = [[[] for _ in range(n)] for _ in range(n)]
    v = set()
    for fireball in fireballs:
        r,c,m,s,d = fireball
        nr = (r + s * dir[d][0]) % n
        nc = (c + s * dir[d][1]) % n
        board[nr][nc].append((m,s,d))
        v.add((nr,nc))
    return board,v

# 2
def work(board,v):
    fireballs = []
    for r,c in v:
        cnt = len(board[r][c])
        if cnt > 1:
            total_m = 0
            total_s = 0
            flag_d = 0
            for m,s,d in board[r][c]:
                total_m += m
                total_s += s
                if d % 2:
                    flag_d += 1
                else:
                    flag_d += 2
            m = total_m // 5
            if m > 0:
                s = total_s // cnt
                if flag_d == cnt or flag_d == 2 * cnt:
                    for i in range(0,7,2):
                        fireballs.append((r,c,m,s,i))
                else:
                    for i in range(1,8,2):
                        fireballs.append((r,c,m,s,i))
        else:
            fireballs.append((r,c,board[r][c][0][0],board[r][c][0][1],board[r][c][0][2]))
    
    return fireballs

for _ in range(k):
    board,v = move(fireballs)
    fireballs = work(board,v)
answer = 0
for fireball in fireballs:
    answer += fireball[2]
print(answer)

'''
--------------------------------------------------------------
NxN격자, 파이어볼 M개 발사
파이어볼의 위치:(r,c)
질량:m
방향:d
속력:s
격자의 행과 열은 1번~N번
*주의: 1번과 N번은 연결되어 있음
파이어볼의 방향은
7 0 1
6   2
5 4 3
명령하면
1. 방향d 속력s칸만큼 이동(같은 칸에 있는 것 가능)
2. 같은 칸에 여러 개 있으면,
- 모두 하나로 합쳐진다
- 4개로 나눠진다
- 나눠진 파이어볼의 질량은 전체/5, 속력은 전체/개수, 방향은 모두홀or짝이면 0 2 4 6/ 나머지 1 3 5 7
상어가 k번 명령, 남아있는 질량의 합 구하기

N,M,K = map(int,input().split())
arr = [[[] for _ in range(N+1)] for _ in range(N+1)]
dis = {0:(-1,0),1:(-1,1),2:(0,1),3:(1,1),4:(1,0),5:(1,-1),6:(0,-1),7:(-1,-1)}


for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    arr[r-1][c-1].append((m,s,d))


for _ in range(K):
    lst = []
    # 이동
    for i in range(N):
        for j in range(N):
            while arr[i][j]:
                m,s,d = arr[i][j].pop()
                nx = (i + dis[d][0]*s) % N
                ny = (j + dis[d][1]*s) % N
                lst.append((nx,ny,m,s,d))

    for nx,ny,m,s,d in lst:
        arr[nx][ny].append((m,s,d))
    
    # 나눠주기
    new_m = 0
    new_s = 0
    odd = 0
    even = 0
    lst2 = []

    for i in range(N):
        for j in range(N):
            
            if len(arr[i][j]) >= 2:
                n = len(arr[i][j])

                for a,b,c in arr[i][j]:
                    new_m += a
                    new_s += b
                    if c%2:
                        odd += 1
                    else:
                        even += 1

                new_m //= 5
                new_s //= n
                arr[i][j].clear()
                if odd == n or even == n: # 0 2 4 6
                    lst2.append((i,j,new_m,new_s,0))
                    lst2.append((i,j,new_m,new_s,2))
                    lst2.append((i,j,new_m,new_s,4))
                    lst2.append((i,j,new_m,new_s,6))
                    

                else: # 1 3 5 7
                    lst2.append((i,j,new_m,new_s,1))
                    lst2.append((i,j,new_m,new_s,3))
                    lst2.append((i,j,new_m,new_s,5))
                    lst2.append((i,j,new_m,new_s,7))

    for i,j,m,s,d in lst2:
        arr[i][j].append((m,s,d))
    
    for i in range(N):
        for j in range(N):
            for m,s,d in arr[i][j]:
                if m == 0:
                    arr[i][j].pop(0)

print(arr)
ans = 0
for i in range(N):
    for j in range(N):
        for m,s,d in arr[i][j]:
        ans += m

print(ans)
'''