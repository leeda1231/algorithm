**목차**

- [정렬](#정렬)



# 정렬

특정한 기준에 따라 데이터를 늘어놓는 알고리즘



## 버블 정렬

바로 옆에 있는 것과 비교해서 정렬하는 것  **O(n<sup>2</sup>)**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
```

💡맨 끝에 가장 큰 수를 놓는 방식



## 선택 정렬

배열에서 작은 데이터를 선별해서 앞으로 보내는 정렬 **O(n<sup>2</sup>)**

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
```

💡맨 끝에 가장 작은 수를 놓는 방식

💡버블 정렬과 시간 복잡도는 동일하지만 자료의 Swap을 반복하는 버블 정렬보단 조금 빠르다.



## 삽입 정렬

자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘 **O(n<sup>2</sup>) or O(n)**

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
```

💡보통의 경우 삽입 정렬보다 퀵 정렬이 효율적이나 정렬이 거의 되어 있는 상황에서는 퀵 정렬 알고리즘보다 더 강력



## 퀵 정렬

무작위로 선정된 한 원소(pivot 역할)을 사용하여 배열을 분할. 선정된 원소보다 작은 원소들은 앞에, 큰 원소들은 뒤에 보낸다.  **O(nlogn) or O(n<sup>2</sup>)**

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left,right,equal = [],[],[]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    return quick_sort(left) + equal + quick_sort(right)
```



## 병합 정렬



## 힙 정렬



## 카운팅 정렬

정렬할 배열에 1~k까지의 정수가 있다면, 각 숫자별로 몇 번씩 나왔는지 count하고, 이 카운팅이 입력된 별도의 배열을 바탕으로 정렬을 하는 것. **O(n)**

```python
def counting_sort(arr):
    m = max(arr)
    count = [0] * (m+1)
    for a in arr:
        count[a] += 1
    i = 0
    for x in range(m):
        for c in range(count[x]):
            arr[i] = a
            i += 1
    return arr
```

💡 메모리 소모 有 : 정렬할 원소의 최소값~최대값까지의 공간이 필요





[참고]

https://modulabs.co.kr/blog/algorithm-python/

https://velog.io/@jinh2352/%EC%A0%95%EB%A0%AC-%EA%B8%B0%EB%B3%B8