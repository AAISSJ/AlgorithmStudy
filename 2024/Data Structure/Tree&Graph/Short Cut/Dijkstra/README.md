# Dijkstra

- 두 노드 간의 최단 거리(최소가 되는 가중치의 합) 구하기 (**우선순위 큐** 사용!)
- 다익스트라의 시간복잡도 Elog(V)
- 기본 로직 -> 쉽게 말하자면 **우선순위 큐 쓴 BFS + weight 배열 고려**
  - graph 배열, visited 배열, **weight 배열** 초기화
  - 시작 노드의 인접노드 u를 우선순위 큐에 저장
  - weight 업데이트 
- **<-> 최소 신장 트리의 Prim 알고리즘 코드와 비슷하지만 차이점 구별하기!**
  - dijkstra는 시작 노드에 대해서 각 노드에 대한 최단 경로를 Weight 배열에 업데이트 ([백준 1713번](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Short%20Cut/Dijkstra/1753.py))
  - prim의 경우는 시작 노드에 대해소 모든 노드를 거쳐서 각 노드를 거쳤을 때의 값을 weight 배열 기록 ([백준 1922](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Minimum%20Spanning%20Tree/Prim/1922.py))
