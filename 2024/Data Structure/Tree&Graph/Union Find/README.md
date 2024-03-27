# Union Find (Disjoint Set, 서로소 집합)
-  Union Find : 두 노드가 같은 그래프에 속하는지 판별하는 알고리즘 (서로소 집합을 찾아내는 알고리즘)
  -  노드를 합치는 Union연산과 노드의 루트 노드를 찾는 Find연산으로 이루어짐

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/4b7f9c95-171c-4818-8df2-ece956eb01ca)


- **코테 활용**
  - Union Find를 활용하여 양방향 그래프에서 **cycle 여부**를 판단할 수 있다.
    - 각 간선의 두 노드의 루트 노드를 확인한다.
      - 루트노드가 서로 다르면 union 연산 실행
      - **루트노드가 서로 같으면 cycle 발생한 것**
## 1. 개념 및 기본 원리 
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/7260d13f-1b8d-4d3b-9341-afb24a4117e2)

### 1) init 연산
``` python
  arr = [i for i in range(N+1)]
```
### 2) Union 연산  
``` python
  def union(a,b):
    a_root = find(a)
    b_root = find(b)
    arr[a_root] = b_root
```
### 3) Find 연산
- **경로압축-최적화 코드**
``` python
  def find(a):
    if arr[a]==a :
        return a 
    else: 
        arr[a]=find(arr[a])
        return arr[a]
```
- 최적화 전 코드
``` python
  def find(a):
      if arr[a] == a:
          return a
      else:
          return find(arr[a])
```
  - 이 버전에서는 arr[a]를 직접 갱신하지 않고, 단순히 재귀적으로 루트 노드를 찾아 반환합니다.
    - 이 방식은 함수가 호출될 때마다 매번 루트 노드까지 재귀적으로 탐색해야 하므로, 깊이가 깊은 트리에서는 비효율적일 수 있습니다. 

<br>

## 2. 시간 복잡도 & 알아둬야 할 것 - "경로 압축"

- 유니온 파인드의 시간 복잡도는 구하기가 꽤 까다롭다.
  - 최적화 여부, 순서 등에 따라 매번 달라지기 때문이다.
  - 코드를 살펴보면 전체 시간 복잡도와 Union 함수의 시간 복잡도는 Find 함수의 시간 복잡도에 따라 결정되는 것을 알 수 있다.




- **경로 압축 최적화를 하지 않은 경우,**
  -  트리가 한 쪽으로 치우칠 수 있기 때문에 Find 함수의 시간 복잡도는 **최악의 경우 O(N)**이다.
-  **경로 압축 최적화를 한 경우,**
  -  트리가 짧고 넓은 형태가 될 가능성이 높아지므로 **O(logN)** 정도로 생각할 수 있겠다.







