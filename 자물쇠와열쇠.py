def solution(key, lock):
    m = len(key)
    n = len(lock)
    # 회전
    def rotate(array, d):
        # n = len(array)
        result = [[0]*n for _ in range(n)]
        if d == 0:
            for r in range(n):
                for c in range(n):
                    result[r][c] = array[r][c]
        if d == 1:
            for r in range(n):
                for c in range(n):
                    result[c][n-r-1] = array[r][c]
        if d == 2:
            for r in range(n):
                for c in range(n):
                    result[n-r-1][n-c-1] = array[r][c]          
        if d == 3:
            for r in range(n):
                for c in range(n):
                    result[n-c-1][r] = array[r][c]
        return result
    
    # 확인
    def check(array):
        for i in range(n):
            for j in range(n):
                if array[i+m-1][j+m-1] != 1:
                    return False
        return True
        
    # 큰 자물쇠 만들기
    big_lock = [[0]*(n+(m-1)*2) for _ in range(n+(m-1)*2)]
    for i in range(n):
        for j in range(n):
            big_lock[i+m-1][j+m-1] += lock[i][j]

    # 자물쇠와 열쇠 합치기
    for i in range(n+m-1):
        for j in range(n+m-1):
            for d in range(4):
                r_key = rotate(key,d)
                for x in range(m):
                    for y in range(m):
                        big_lock[i+x][j+y] += r_key[x][y]
                
                if check(big_lock):
                    return True
                
                for x in range(m):
                    for y in range(m):
                        big_lock[i+x][j+y] -= r_key[x][y]
    
    return False   
