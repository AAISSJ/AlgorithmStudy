
# 이분 탐색(이진 탐색, Binary Search) & Parametric Search 

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/2c82b3c6-9b48-4039-baf8-bd4bce696379)

- 만약 해시 탐색으로도 해결되지 않는 입력 범위라면? -> "이분 탐색"
  - O(logN)의 시간 복잡도를 가짐
- 단, **데이터가 정렬되어있어야 함** 
- 중요한 특징 중 하나 : **lower bound & upper bound**

## 시간 복잡도 
- O(logN)의 시간 복잡도를 가짐

<br>

## 이분 탐색의 기본 코드 
```python
def binary_search(target, data):
    data.sort()
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end: # start가 end보다 커지는 경우 가리킴 
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return mid 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
           end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
           start = mid + 1
    return -1 # target이 배열에 없는 경우
```

## lower bound & upper bound

## lower bound 
- lower bound : target값이 처음 나오는 인덱스 반환 
- 아래 두 코드 간 차이점 잘 보기 !
```python
def lower_bound(arr, x):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid
    return end
```
```python
def lower_bound_while_end(arr, x):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return end
```


## upper bound 
- upper bound : target보다 큰 값이 처음 나오는 인덱스 반환
  - target값보다 같은 경우에도 더 큰 값을 찾으러 옮겨야 된다 `if arr[mid] <= x:`
- 아래 두 코드 간 차이점 잘 보기 !

```python
def upper_bound(arr, x):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= x: 
            start = mid + 1
        else:
            end = mid
    return end
```

```python
def upper_bound_while_end(arr, x):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return end
```

# Parametric Search 
- 파라메트릭 서치는 **최적화 문제를 결정 문제로 바꾸어 풀어 나가는 기법**
  - **최적화 문제의 예 : 최대값 또는 최소값을 찾는 문제**
  - **결정 문제 : "예" 또는 "아니오"로 답할 수 있는 문제**
- 파라메트릭 탐색은 **주로 정답이 될 수 있는 범위 내에서 조건을 만족하는 최적의 값을 찾을 때 사용**
  - 예를 들어, 어떤 조건을 만족하는 최대 길이를 찾는 문제에서 최적의 길이를 찾기 위해 파라메트릭 탐색을 사용
  
## 이분 탐색과의 차이점  
- 간단히 말하면, 파라메트릭 탐색은 이분 탐색을 특정한 유형의 문제 해결 방식에 적용한 것이며, 이분 탐색보다 더 일반적이고 복잡한 문제에 접근할 수 있는 방법을 제공합니다.
  - 적용 문제 유형: 이분 탐색은 주로 정렬된 리스트에서 특정 값을 찾는 문제에 사용됩니다. 반면, 파라메트릭 탐색은 최적화 문제를 결정 문제로 변환하여, 이분 탐색을 통해 최적의 값을 찾는 데 사용됩니다.
  - 목적: 이분 탐색의 주된 목적은 데이터 내에서 특정 값의 존재 여부나 위치를 찾는 것입니다. 파라메트릭 탐색은 최적화 문제에 대한 최적의 해(예: 최소값, 최대값)를 찾는 데 초점을 맞춥니다.
  - 작동 원리: 이분 탐색은 데이터의 범위 내에서 중간점을 찾아 탐색 범위를 줄여 나가는 방식으로 작동합니다. 파라메트릭 탐색은 이분 탐색의 원리를 사용하지만, 최적화 문제의 해를 찾기 위해 탐색 범위 내에서 조건을 만족하는 최적값을 찾아나가는 과정에 초점을 맞춥니다.


# 읽어볼만한 글

- [이분 탐색(Binary Search) 헷갈리지 않게 구현하기 ](https://www.acmicpc.net/blog/view/109)
- [Parametric Search](https://heytech.tistory.com/97)
