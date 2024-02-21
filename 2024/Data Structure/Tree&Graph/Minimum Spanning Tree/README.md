
# 최소 신장 트리(최소 스패닝 트리, Minimum Spanning Tree)
-  무방향 그래프의 간선들에 가중치가 주어진 경우, 여러 신장 트리 중에 **간선들의 가중치 합이 최소**인 신장 트리


## 1. Kruskal
-  모든 간선을 **가중치 기준으로 오름차순으로 정렬(우선순위 큐)**하고, 이 간선들을 순서대로 모든 정점이 연결될 때까지 연결하는 것이다.
  - **단, 트리기 때문에 사이클을 이루지 않는다(Union Find)**
-  **우선 순위 큐 + Union Find** 이용하여 구현! 


## 2. Prim 
- **<-> 최단 경로 알고리즘의 dijkstra와 코드 비슷하나 차이점 확인하기!**
  - dijkstra는 시작 노드에 대해서 각 노드에 대한 최단 경로를 Weight 배열에 업데이트 ([백준 1713번](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Short%20Cut/Dijkstra/1753.py))
  - prim의 경우는 시작 노드에 대해소 모든 노드를 거쳐서 각 노드를 거쳤을 때의 값을 weight 배열 기록 ([백준 1922](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Minimum%20Spanning%20Tree/Prim/1922.py))
