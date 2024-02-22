from heapq import *
import sys
input = sys.stdin.readline 


V,E = map(int, input().split())


# 2. 프림 - 우선 순위 큐 + weight 배열
# 1. 그래프 초기화 like DFS 

graph = {i:[] for i in range(1, V+1)}
visited = [0 for i in range(V+1)]

# weight 정보도 포함해서 인접행렬에 값 넣어주기 
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

def prim(root):
    total = 0 
    pq = [(0,root)] 
    heapify(pq)
    
    while pq:
        now_w, now_n = heappop(pq)
        if not visited[now_n] : 
            visited[now_n]=1
            total+= now_w
            for next_w, next_n in graph[now_n]:
                if not visited[next_n]:
                    heappush(pq,(next_w,next_n))
    return total
total=prim(1)
print(total)
