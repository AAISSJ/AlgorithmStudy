
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
  - target값보다 같은 경우에도 더 작은 값을 찾으러 옮겨야 된다 `else:`
  - return은 end로 !
    - `end`를 반환하는 이유는, 반복이 종료될 때 end는 x를 초과하는 요소 바로 이전 위치를 가리키기 때문
    - `mid`를 반환하지 않는 이유는, 반복문이 종료되었을 때 mid는 최종적으로 검사된 중간 위치를 가리키지만, 이 위치가 항상 x를 초과하는 첫 번째 요소를 정확히 가리키는 것은 아님
    - `start`를 반환하지 않는 이유는, 반복문이 종료될 때 start는 x를 초과하는 첫 번째 요소의 위치보다 하나 더 큰 상태이기 때문
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
- 조건에 만족하는 가장 큰 값을 반환하기 위해서 return은 end로 !

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
- 파라메트릭 서치는 이분 탐색의 개념을 활용하여, **최적화 문제를 결정 문제로 바꾸어 풀어 나가는 기법**
  - **최적화 문제의 예 : 최대값 또는 최소값을 찾는 문제**
  - **결정 문제 : "예" 또는 "아니오"로 답할 수 있는 문제**
- 파라메트릭 탐색은 **주로 정답이 될 수 있는 범위 내에서 조건을 만족하는 최적의 값을 찾을 때 사용**
  - 예를 들어, 어떤 조건을 만족하는 최대 길이를 찾는 문제에서 최적의 길이를 찾기 위해 파라메트릭 탐색을 사용

```python

  start, end = 0, len(arr) - 1
  while start <= end:
      mid = (start + end) // 2

      # check 함수를 이용한 어떤 조건 -> 주로 정답이 될 수 있는 범위 내에서 조건을 만족하는지 !
      if ~~~~~ :
          start = mid + 1
      else:
          end = mid - 1
  return end


```


# 읽어볼만한 글

- [이분 탐색(Binary Search) 헷갈리지 않게 구현하기 ](https://www.acmicpc.net/blog/view/109)
- [Parametric Search](https://heytech.tistory.com/97)
