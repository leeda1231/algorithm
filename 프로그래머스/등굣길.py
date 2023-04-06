# n: 행, m: 열
def solution(m, n, puddles):
    
    arr = [[0]*(m+1) for _ in range(n+1)]
    arr[1][1] = 1
    
    for x,y in puddles: # 행열주의
        arr[y][x] = -1
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            
            if arr[i][j] == -1:
                arr[i][j] = 0
                continue
            
            arr[i][j] += arr[i][j-1] + arr[i-1][j]
            
    answer = arr[n][m] % 1000000007
    
    return answer