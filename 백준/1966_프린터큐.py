from collections import deque

T = int(input())

for tc in range(T):
    n, m = map(int,input().split())
    imp = deque(list(map(int,input().split())))
    idx = deque([i for i in range(n)])
    cnt = 0

    while imp: # imp가 비어있지 않다면 반복
        
        if imp[0] == max(imp): # 첫 번째 요소가 최대값이면
            cnt += 1           # 인쇄하고 순서 더해줌
            imp.popleft()      # 없앰
            if idx.popleft() == m:   # 구하고자 하는 값과 같다면, idx.popleft도 됨.
                print(cnt)           # 인쇄 순번 출력
        
        else:                           # 최대값 아니면
            imp.append(imp.popleft())   # 없애고 뒤로 보내기
            idx.append(idx.popleft())   # 인덱스도 마찬가지
