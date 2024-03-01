
# 이분 탐색(이진 탐색, Binary Search)

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/2c82b3c6-9b48-4039-baf8-bd4bce696379)

- 만약 해시 탐색으로도 해결되지 않는 입력 범위라면? -> "이분 탐색"
  - O(logN)의 시간 복잡도를 가짐
- 단, **데이터가 정렬되어있어야 함** 
- 중요한 특징 중 하나 : **lower bound & upper bound**

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

### lower bound 
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/3d3d92c9-817f-4092-bfd6-5107375ad42b)
- lower bound : target값이 처음 나오는 인덱스 반환 
-  
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


### upper bound 

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



# 읽어볼만한 글

- [이분 탐색(Binary Search) 헷갈리지 않게 구현하기 ](https://www.acmicpc.net/blog/view/109)
