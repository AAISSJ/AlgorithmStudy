
# 최단 거리 알고리즘
- 그래프 상의 **노드 간의** 탐색 비용 최소화하는 알고리즘
- 종류 3가지
  - 다익스트라(Dijkstra)
  - 플로이드 워셜(Floyd Warshall)
  - 벨만 포드(Bellman Ford)
- 연결하는 비용 최소 -> 최단 경로 or 최소 신장 트리 -> 최소 스패닝 트리와의 차이점 ?
  - **최단 경로 : 가중 그래프 상의 두 노드를 연결하는 가장 짧은 경로를 찾는 방법 / 방향&무방향**
  - 최소 신장 트리 : 가중 그래프 상의 **모든 노드들을 최소 비용으로 연결**하는 방법 / **무방향 only**



## 1. 다익스트라(Dijkstra)
- 두 노드 간의 최단 거리(최소가 되는 가중치의 합) 구하기 (**우선순위 큐** 사용!)
- 다익스트라의 시간복잡도 Elog(V)
- 기본 로직 -> 쉽게 말하자면 **우선순위 큐 쓴 BFS + weight 배열 고려**
  - graph 배열, visited 배열, **weight 배열** 초기화
  - 시작 노드의 인접노드 u를 우선순위 큐에 저장
  - weight 업데이트 
- **<-> 최소 신장 트리의 Prim 알고리즘 코드와 비슷하지만 차이점 구별하기!**
  - dijkstra는 시작 노드에 대해서 각 노드에 대한 최단 경로를 Weight 배열에 업데이트 ([백준 1713번](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Short%20Cut/Dijkstra/1753.py))
  - prim의 경우는 시작 노드에 대해소 모든 노드를 거쳐서 각 노드를 거쳤을 때의 값을 weight 배열 기록 ([백준 1922](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Minimum%20Spanning%20Tree/Prim/1922.py))

## 2. 플로이드 워셜(Floyd Warshall)
- 모든 시작점에 대해서! 


## 3. 벨만 포드(Bellman Ford)
- 가중치의 값 중에 음수가 존재할 때 


