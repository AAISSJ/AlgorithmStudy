# 최소 신장 트리(최소 스패닝 트리, Minimum Spanning Tree)
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/b6c9530c-24ab-4784-9aec-c3f54361b4a4)

-  **무방향 그래프**의 간선들에 가중치가 주어진 경우, 여러 신장 트리 중에 **간선들의 가중치 합이 최소**인 신장 트리
-  <-> 최단 경로 알고리즘과의 차이점 !
  -  최단 경로 알고리즘은, 가중 그래프 상의 임의의 두 노드를 연결하는 가장 짧은 경로를 찾는 방법 / 방향&무방향
  -  그러나, 최소 신장 트리 : 그래프 상의 모든 노드들을 최소 비용으로 연결하는 방법 / 무방향 only


## 1. Kruskal
-  모든 간선을 **가중치 기준으로 오름차순으로 정렬**하고, 이 간선들을 순서대로 **모든 정점이 연결될 때까지 연결하는 것**이다.
  - **단, 트리기 때문에 사이클을 이루지 않는다(Union Find)**
-  **sort + Union Find** 이용하여 구현! 


## 2. Prim 
- **BFS+우선 순위 큐** 이용하여 구현!
- **<-> 최단 경로 알고리즘의 dijkstra와 코드 비슷하나 차이점 확인하기!**
  - dijkstra는 시작 노드에 대해서 각 노드에 대한 최단 경로를 Weight 배열에 업데이트 ([백준 1713번](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Short%20Cut/Dijkstra/1753.py))
  - prim의 경우는 시작 노드에 대해서 모든 노드를 거쳐서 각 노드를 거쳤을 때의 값을 기록 ([백준 1922](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Minimum%20Spanning%20Tree/Prim/1922.py))
