from heapq import * 
import sys 
input = sys.stdin.readline 

# 무방향 
# 나머지 길의 유지비의 합을 최소
# => MST (크루스칼, 프림)
    # 크루스칼 - union find 사용 - 사용 조건: 간선이 적을 때 (간선 정렬하는 과정 때문에)
    # 프림 - dijkstra 처럼 pq 사용 - 사용 조건: 정점이 적을 때 (시작 노드에 대해서 모든 노드를 거쳐서 각 노드를 거쳤을 때의 값)
# 문제 풀이 - MST 구하기 그 중 가장 비용이 큰 길을 없애기 (분할 -> 2개로)
    # 본 문제는 집의 개수 N이 100,00으로 더 작으므로 프림로 푼다 

# 0. 입력 받기 
N, M = map(int, input().split())
graph ={i:[] for i in range(1,N+1)}
visited = [0 for i in range(N+1)]

for i in range(M):
    A,B,C = map(int, input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

# 1. prim 
def prim(root):
    cnt = 0 
    max_w= 0
    pq = [(0,root)]
    # visited[root]=1
    heapify(pq)
    while pq:
        now_w, now_n = heappop(pq)
        if not visited[now_n]:
          visited[now_n]= 1
          cnt += now_w
          if max_w < now_w:
            max_w = now_w
          
          for next_w, next_n in graph[now_n]:
            heappush(pq, (next_w, next_n))
    return cnt,  max_w

cnt, max_w= prim(1)
print(cnt - max_w)
