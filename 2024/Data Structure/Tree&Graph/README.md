
# GRAPH


## Union Find
-  Union Find : 두 노드가 같은 그래프에 속하는지 판별하는 알고리즘 (서로소 집합을 찾아내는 알고리즘)
  -  노드를 합치는 Union연산과 노드의 루트 노드를 찾는 Find연산으로 이루어짐
- **코테 활용**
  - Union Find를 활용하여 양방향 그래프에서 cycle 여부를 판단할 수 있다.
    - 각 간선의 두 노드의 루트 노드를 확인한다.
      - 루트노드가 서로 다르면 union 연산 실행
      - 루트노드가 서로 같으면 cycle 발생한 것



## Directed Acyclic Graph (DAG) + 위상 정렬(Topology Sort)
- Directed Acyclic Graph (DAG) : 순환(Cycle)을 가지지 않는 방향 그래프
- 위상 정렬(Topology Sort) : DAG에서 그래프의 방향성을 거스르지 않고 정점들을 나열하는 것
  - 시간 복잡도는 **O(V+E)**
  - 위상 정렬에서는 여러 가지 답이 있을 수 있음 (한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상 있는 경우!)
  - 그래프에서 사이클이 발생할 경우, 그 사이클이 발생한 정점은 감소시킬 수 없는 진입 차수를 갖게 되므로 위상 정렬의 진행이 멈추게 된다.
- **코테 활용**
  - 위상 정렬은 **어떠한 Task들 간의 먼저 이행되어야하는 순서가 존재**할 때, 이를 올바른 순서로 진행하기 위해 사용
  - 선행 관계 등이 제시될 경우 위상 정렬 문제로 접근할 수 있음


## 최소 신장 트리(최소 스패닝 트리, Minimum Spanning Tree)
-  무방향 그래프의 간선들에 가중치가 주어진 경우, 여러 신장 트리 중에 **간선들의 가중치 합이 최소**인 신장 트리


### 1. Kruskal
-  모든 간선을 **가중치 기준으로 오름차순으로 정렬(우선순위 큐)**하고, 이 간선들을 순서대로 모든 정점이 연결될 때까지 연결하는 것이다.
  - **단, 트리기 때문에 사이클을 이루지 않는다(Union Find)**
-  **sort + Union Find** 이용하여 구현! 


### 2. Prim 
- **BFS+우선 순위 큐** 이용하여 구현!
- **<-> 최단 경로 알고리즘의 dijkstra와 코드 비슷하나 차이점 확인하기!**
  - dijkstra는 시작 노드에 대해서 각 노드에 대한 최단 경로를 Weight 배열에 업데이트 ([백준 1713번](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Short%20Cut/Dijkstra/1753.py))
  - prim의 경우는 시작 노드에 대해서 모든 노드를 거쳐서 각 노드를 거쳤을 때의 값을 기록 ([백준 1922](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Minimum%20Spanning%20Tree/Prim/1922.py))

