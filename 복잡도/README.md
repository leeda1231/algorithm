# 복잡도

알고리즘의 성능을 나타내는 척도



## 1. 시간 복잡도

**개념**

- 특정한 크기의 입력에 대해서 알고리즘이 얼마나 오래 걸리는지
- 알고리즘을 위해 필요한 연산의 횟수



시간 제한이 1초인 경우

- N이 10,000,000일 때, O(N)인 알고리즘 설계하면 문제 풀 수 있다.



수행 시간 측정 소스코드

```python
import time
start_time = time.time()
# 프로그램 소스코드
end_time = time.time()
print(start_time - end_time)
```



## 2. 공간 복잡도

**개념**

- 특정한 크기의 입력에 대해서 알고리즘이 얼마나 많은 메모리를 차지하는지
- 알고리즘을 위해 필요한 메모리의 양



보통 메모리 사용량 128 ~ 512MB

파이썬 리스트의 크기가 1,000만 단위 이상이라면 넘어간다.

=> 메모이제이션