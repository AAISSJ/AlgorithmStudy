# 연결하는 비용 최소 -> 최단 경로 or 최소 신장 트리 
    # 최단 경로 : 가중 그래프 상의 두 노드를 연결하는 가장 짧은 경로를 찾는 방법 / 방향&무방향
    # 최소 신장 트리 : 그래프 상의 모든 노드들을 최소 비용으로 연결하는 방법 / 무방향 only
# 본 문제에서는 모든 컴퓨터를 연결하는 데 필요한 최소 비용이므로 최소 신장 트리 
    # 크루스칼 또는 프림 알고리즘을 이용하면 되겠다 

from heapq import *
 
N = int(input())
M = int(input())


# 1. 그래프 초기화 like DFS 
graph = {i:[] for i in range(1,N+1)}
visited = [0 for i in range(N+1)]
weight = [10001 for i in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))


def prim(node):
    # 처음 시작 노드 PQ 에 넣어주기 & 가중치는 0 
    weight[node] = 0 
    pq = [(0, node)]
    heapify(pq) 
    
    # 아래로 내려가기 
    while pq: 
        now_w, now_n = heappop(pq)
        if not visited[now_n]:
            visited[now_n]=1
            for next_w, next_n in graph[now_n]:
                if not visited[next_n] and weight[next_n]>next_w:
                    weight[next_n]=next_w
                    heappush(pq,(next_w, next_n))

prim(1) # 1부터 시작 - 그냥 임의로 
print(sum(weight[1:]))
    
    
