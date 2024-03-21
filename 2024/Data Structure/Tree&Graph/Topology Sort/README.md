
# Directed Acyclic Graph (DAG) + 위상 정렬(Topology Sort)

## Directed Acyclic Graph (DAG) : 순환(Cycle)을 가지지 않는 "방향" 그래프

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/b0362f2d-996e-4f9f-991f-c18979640b56)

<br>

## 위상 정렬(Topology Sort) : DAG에서 그래프의 방향성을 거스르지 않고 정점들을 나열하는 것

### 1. 개념 및 기본 원리 
- 1. init : graph와 in_degree 배열 초기화
- 2. topology sort (BFS의 변형)
  - 1) queue를 이용하여 진입 차수가 0인 노드부터 먼저 큐에 넣기
  - 2) 현 노드에서 진입 차수 하나씩 빼고 0이 된다면 큐에 넣어주기
  
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

