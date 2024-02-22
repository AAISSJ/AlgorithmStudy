# 조건 -> Dijkstra 
  # 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다
  # 최단 거리로 이동
  # 가중치 c (1 ≤ c ≤ 1,000) 
  

from heapq import *

N, E = map(int,input().split()) # 정점, 간선 
graph= {i:[] for i in range(1,N+1)}

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))


def dijstra(node):
    weight = [10**10 for i in range(N+1)]
    pq = [(0,node)]
    heapify(pq)
    weight[node] = 0 
    while pq:
        now_w, now_n = heappop(pq)
        if now_w > weight[now_n]: 
            continue
        for next_w, next_n in graph[now_n]:
            if next_w+now_w< weight[next_n]:
                weight[next_n] = next_w+now_w
                heappush(pq, (weight[next_n],next_n))
    
    return weight

v_1,v_2 = map(int, input().split())

weight_1 = dijstra(1)
weight_v1 =  dijstra(v_1)
weight_v2 =  dijstra(v_2)

# print(weight_1)
# print(weight_v1)
# print(weight_v2)

path1= weight_1[v_1]+weight_v1[v_2]+weight_v2[N]
path2= weight_1[v_2]+weight_v2[v_1]+weight_v1[N]

answer = min(path1, path2)
if answer>=10**10:
    print(-1)
else: 
    print(answer)
