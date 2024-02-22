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

        # **** bfs, prim과 다른 점 - 중복 체크하지 않음(이미 방문한 정점이어도 최단 경로면 pq에 추가), 그 대신 weight가 최소인지 확인 
        if weight[now_n] < now_w: # 최단거리 테이블( distance[꺼낸 노드번호] ) 에 기록된 정보보다 값이 크면, 최단거리 정보가 아니기 때문에 continue 로 무시
            continue 
        # ****************** 
        
        # 그게 아니라면 최단거리 정보이므로 다음과 같은 작업을 수행
        for next_w, next_n in graph[now_n]: # 꺼낸 노드번호에서 갈수 있는 노드와 거리정보를 i를 통해 한개씩 접근
            # **** bfs, prim과 다른 점 
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



