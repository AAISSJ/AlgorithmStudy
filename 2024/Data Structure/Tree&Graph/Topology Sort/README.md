
# Directed Acyclic Graph (DAG) + 위상 정렬(Topology Sort)

## Directed Acyclic Graph (DAG) : 순환(Cycle)을 가지지 않는 "방향" 그래프

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/b0362f2d-996e-4f9f-991f-c18979640b56)

<br>

## 위상 정렬(Topology Sort) : DAG에서 그래프의 방향성을 거스르지 않고 정점들을 나열하는 것

### 1. 개념 및 기본 원리 
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/eb1d6c91-9835-43f3-8247-f76e3bbe212b)

1. 진입 차수가 0인 정점(즉, 들어오는 간선의 수가 0)을 선택
  - 진입 차수가 0인 정점이 여러 개 존재할 경우 어느 정점을 선택해도 무방하다.
  - 초기에 간선의 수가 0인 모든 정점을 큐에 삽입
2. 선택된 정점과 여기에 부속된 모든 간선을 삭제
  - 선택된 정점을 큐에서 삭제
  - 선택된 정점에 부속된 모든 간선에 대해 간선의 수를 감소
3. 위의 과정을 반복해서 모든 정점이 선택, 삭제되면 알고리즘 종료

https://gmlwjd9405.github.io/2018/08/27/algorithm-topological-sort.html
  
- 위상 정렬에서는 여러 가지 답이 있을 수 있음 (한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상 있는 경우!)
  - 그래프에서 사이클이 발생할 경우, 그 사이클이 발생한 정점은 감소시킬 수 없는 진입 차수를 갖게 되므로 위상 정렬의 진행이 멈추게 된다.
 
### 2. 시간복잡도
- 시간 복잡도는 **O(V+E)**

<br>

### 3. 코드 
``` python
from collections import deque 


N, M = map(int, input().split())

arr = [[] for i in range(N+1)]
in_degree = [0 for i in range(N+1)] # 진입차수


def init(a,b):
    arr[a].append(b)
    in_degree[b]+=1

# init
for _ in range(M):
    A,B =  map(int, input().split())
    init(A,B)
    
# print(arr)
# print(in_degree)

# topological sort
def topology_sort():
    result = [] 
    queue = deque()
    # 처음 시작할 떄는 진입 차수가 0인 노드를 먼저 큐에 넣기 
    for i in range(1, N+1):
        if in_degree[i]==0 : # 진입차수가 0이라면 == 리프노드라면 
            queue.append(i)
    
    # 큐가 빌 때까지 
    while queue:
        now = queue.popleft()
        result.append(now)
        print(now, end=' ')
        
        for next_one in arr[now]:
            in_degree[next_one]-=1
            if in_degree[next_one] == 0 : # 새롭게 진입차수가 0이 되는 노드들을 삽입
                queue.append(next_one)

topology_sort()

```


### 4. **코테 활용**
  - 위상 정렬은 **어떠한 Task들 간의 먼저 이행되어야하는 순서가 존재**할 때, 이를 올바른 순서로 진행하기 위해 사용
  - 선행 관계 등이 제시될 경우 위상 정렬 문제로 접근할 수 있음

