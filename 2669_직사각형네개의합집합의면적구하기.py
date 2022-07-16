a = [[0]*100 for _ in range(100)] # 100x100 좌표
cnt = 0 

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split()) # 입력
    for i in range(x1, x2):
        for j in range(y1, y2):
            if a[i][j] == 0: 
                a[i][j] = 1
                cnt += 1

print(cnt) # 출력

'''
1. 100x100 이차원 배열 만들기
2. 입력값 받기(4번)
3. 반복문으로 입력받은 범위 설정
4. 이차원 배열에 입력값 인덱스 이용하여 1로 바꾸기
5. 0에서 1로 바뀔 때마다 cnt 1씩 추가(중복 방지)
6. cnt 출력
'''