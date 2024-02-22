# 연결하는 비용 최소 -> 최단 경로 or 최소 신장 트리 
    # 최단 경로 : 가중 그래프 상의 두 노드를 연결하는 가장 짧은 경로를 찾는 방법 / 방향&무방향
    # 최소 신장 트리 : 그래프 상의 모든 노드들을 최소 비용으로 연결하는 방법 / 무방향 only
# 본 문제에서는 모든 컴퓨터를 연결하는 데 필요한 최소 비용이므로 최소 신장 트리 
    # 크루스칼 또는 프림 알고리즘을 이용하면 되겠다 

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
                heapq.heappush(queue, (next_wei, next_node))
    return answer

print(Prim())
    
    
