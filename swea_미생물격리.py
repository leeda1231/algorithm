from collections import defaultdict

dir = {1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}

T = int(input())
for tc in range(T):
    n,m,k = map(int,input().split())
    board = defaultdict(list)
    for _ in range(k):
        x,y,num,d = map(int,input().split())
        board[(x,y)] = [[num,d]]

    for _ in range(m):
        # 이동 + 빨간셀
        tmp_board = defaultdict(list)
        for k,v in board.items():
            x,y = k
            num,d = v[0][0],v[0][1]
            nx = x + dir[d][0]
            ny = y + dir[d][1]
            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                # 미생물 죽이기
                num //= 2
                # 방향전환
                if d%2:
                    d += 1
                else:
                    d -= 1
            tmp_board[(nx,ny)].append([num,d])
        # 합치기
        for tk,tv in tmp_board.items():
            if len(tv) > 1:
                new_num = 0
                new_d = 0
                max_v = 0
                for tmp_num,tmp_d in tv:
                    new_num += tmp_num
                    if tmp_num > max_v:
                        max_v = tmp_num
                        new_d = tmp_d
                tmp_board[tk] = [[new_num,new_d]]
        board = tmp_board

    ans = 0
    for value in board.values():
        ans += value[0][0]


    print(f'#{tc+1}',ans)