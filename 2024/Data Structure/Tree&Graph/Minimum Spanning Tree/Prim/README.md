# Prim 알고리즘 
## 1. 개념 및 기본 원리 

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/8ae11b16-fd08-4201-a8c8-861bcef8ebc2)

1. 임의의 간선을 선택
2. 선택한 간선의 정점으로부터 가장 낮은 가중치를 갖는 정점을 선택
3. 모든 정점이 선택될 때까지 반복


<br> 

## 2. 시간 복잡도 
- prim 알고리즘의 시간 복잡도는 O(E log V)
  - 우선 순위 큐에서 간선을 꺼낼 때 logV의 시간이 소요

<img width="703" alt="스크린샷 2024-03-27 오후 1 05 08" src="https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/a88dc9f4-c671-47c5-b074-5f3ee7981e02">

<br> 

## 3. 사용 조건 
- 프림은 정점 위주의 알고리즘, 크루스칼은 간선 위주의 알고리즘
  - 프림의 경우 최소 거리의 정점을 찾는 부분에서 자료구조의 성능에 영향을 받는다.
  - 크루스칼은 간선을 기준으로 정렬하는 과정이 오래 걸린다.
- 간선의 개수가 작은 경우에는 크루스칼, 간선의 개수가 많은 경우에는 프림.

<br> 

## 4. 사용되는 자료구조 및 알고리즘 & 기본 코드
```python
import heapq
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = 0

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

queue = []
heapq.heappush(queue, (0,1))

def Prim():
    global answer
    while queue:
        wei, now = heapq.heappop(queue)

        # ***** dijkstra와의 차이점 - 방문한 곳 또 가면 안된다 -> 사이클 생긴다
        if visited[now] == False:
            visited[now] = True
            answer += wei
            for next_wei, next_node in graph[now]:
                if not visited[next_node]:
                  heapq.heappush(queue, (next_wei, next_node))
    return answer

print(Prim())
    
```
- 왜 if visited[now] == False: 가 필요한가 ?
  - 처음 : 18번째 라인에서 현재 노드와 연결된 간선들을 추가해줄 때 '미방문 노드 간선'만을 heap에 넣어주기 때문에 11번째 라인에서의 최소 간선 노드에 대한 방문 처리를 해주지 않아도 된다고 생각했음
  - 답변 :
    - 프림, 그리고 다익스트라 알고리즘처럼 **힙 (또는 우선선위 큐)를 사용하는 알고리즘**에서는
    - 어떤 원소 u가 힙에 처음 들어갈 때 방문처리 하는게 아니고, **u가 힙에서 처음 빠질 때 방문처리 해야 됩니다**.
    - 프림하고 다익스트라는 크게 보면 탐욕법(그리디) 알고리즘으로 분류할 수 있습니다.
      - 탐욕스럽게 지금 눈 앞에 보이는 가장 좋은 (우선 순위가 가장 높은) 방법들만 택하면서 답을 구하면 전체 답을 알 수 있기 때문
    - 알고리즘이 진행되면서 몇몇 원소들의 우선순위가 바뀔 수 있음 (다익스트라를 예로 들면, 어떤 정점 v까지 최단 경로가 바뀐다는 등)
    - **힙에 넣을 때는 아직 우선순위가 아직 정해지지 않을 수 있습니다.**
    - **하지만, 힙에서 뺄 때는 항상 우선순위가 정해져 있는 상태입니다.**
    - **따라서, 힙에 넣을 때가 아닌, 힙에서 나올 때 방문여부를 처리해야 됩니다.**

<br> 

## 5. 문제 유형 



<br> 

## 6. 다른 알고리즘과의 차이점 
- <-> 최단 경로 알고리즘의 dijkstra와 코드 비슷하나 차이점 확인하기!
  - dijkstra는 시작 노드에 대해서 각 노드에 대한 최단 경로를 Weight 배열에 업데이트 (백준 1713번)
  - prim의 경우는 시작 노드에 대해서 모든 노드를 거쳐서 각 노드를 거쳤을 때의 값을 기록 (백준 1922)
 
## 7. 참고 자료 
- https://8iggy.tistory.com/159
