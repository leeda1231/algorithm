n,k = map(int,input().split())
fish = list(map(int,input().split()))

while 1:
    # 1
    min_val = min(fish)
    for i in range(n):
        if fish[i] == min_val:
            fish[i] += 1
    
    # 2
    # 공중 부양시킨 어항 중 
    # 가장 오른쪽에 있는 어항의 아래에 
    # 바닥에 있는 어항이 있을때까지 반복
    
    
