# Dijkstra

## 1. 개념 & 기본 원리 

- 두 노드 간의 최단 거리(최소가 되는 가중치의 합) 구하기
- bfs와 다른 점
   - 우선 순위 큐를 사용함
   - 중복 체크하지 않음(이미 방문한 정점이어도 최단 경로면 pq에 추가)
   - 현재 기록된 weight 배열의 값보다 현재 값이 더 작다면 갱신

<br>

## 2. 시간 복잡도 
- 다익스트라의 시간복잡도 O(ElogV)

<br>


## 3. 사용 조건
1. 가중치가 있고, 그 가중치가 모두 자연수인 그래프 
2. 주어진 시작점에서 다른 모든 정점으로의 최단 경로
   

<br>


## 4. 사용되는 자료구조 및 알고리즘  & 기본 코드
- 우선순위 큐 + BFS + weight 배열 고려
- 기본 코드 (백준 1753.py)

```python
# 방향 그래프 &  주어진 시작점에서 다른 모든 정점으로의 최단 경로 
# 가중치 값은 모두 자연수 
# -> 다익스트라 
from heapq import *
import sys 

input = sys.stdin.readline 

V, E = map(int, input().split()) # 정점, 간선
K = int(input()) # 시작 정점 

# 1. graph, visited, weight 배열 초기화 
graph = {i:[] for i in range(1, V+1)}
weight = [10**9 for i in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))

# 2. dijkstra 함수 
def dijkstra(start_node):

    # 시작 노드에 대한 초기화 
    weight[start_node] = 0 
    pq = [(0, start_node)]
    heapify(pq)
    
    # 그의 "인접 노드"에 대해서 "가중치 순"으로 차례대로 방문  
    while pq:
        now_w, now_n = heappop(pq)

        # 얘를 고려하는 것도 시간복잡도 차원에서 중요하다ㅇㅇㅇ
        if now_w > weight[now_n]:
            continue
        
        for next_w, next_n in graph[now_n]: # 꺼낸 노드번호에서 갈수 있는 노드와 거리정보를 i를 통해 한개씩 접근
            # **** bfs, prim과 다른 점 -> 현재 기록된 weight 배열의 값보다 현재 값이 더 작다면 갱신 
            if now_w + next_w < weight[next_n]:
                weight[next_n] = now_w + next_w
                # ************************
                heappush(pq,(weight[next_n] ,next_n))

        
dijkstra(K)


# 3. 시작 노드 K와 각 정점 i까지의 최단 거리 출력      
for i in range(1,V+1):
    if weight[i] == 10**9:
        print("INF")
    else:
        print(weight[i])

```


<br>

## 5. 문제 유형 
- 다익스트라 경로 구하기 : https://www.acmicpc.net/problem/11779
- 거꾸로 다익스트라 : https://www.acmicpc.net/problem/1238
- 2차원 다익스트라 : https://www.acmicpc.net/problem/4485
- 한점 거치는 다익스트라 : https://www.acmicpc.net/problem/18223


<br>

## 6. 다른 알고리즘과의 차이점 
- BFS와의 차이점 
- **<-> 최소 신장 트리의 Prim 알고리즘 코드와 비슷하지만 차이점 구별하기!**
  - dijkstra는 시작 노드에 대해서 각 노드에 대한 최단 경로를 Weight 배열에 업데이트 ([백준 1713번](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Short%20Cut/Dijkstra/1753.py))
    -  prim과의 차이점 - 중복 체크하지 않음(이미 방문한 정점이어도 최단 경로면 pq에 추가), **그 대신 지금 가는 길의 weight가 최소가 되는지 확인** 
  - prim의 경우는 시작 노드에 대해서 모든 노드를 거쳐서 각 노드를 거쳤을 때의 값을 기록 ([백준 1922번](https://github.com/AAISSJ/AlgorithmStudy/blob/main/2024/Data%20Structure/Tree%26Graph/Minimum%20Spanning%20Tree/Prim/1922.py))
    - dijkstra와의 차이점 - **방문한 곳 또 가면 안된다**
- 벨만 포드와의 차이점
- 플루이드 와샬과의 차이점

  
