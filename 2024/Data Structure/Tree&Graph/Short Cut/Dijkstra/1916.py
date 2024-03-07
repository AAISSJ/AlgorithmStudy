import sys 
from heapq import *
input = sys.stdin.readline 

# 0. 입력 받기 
N = int(input())
M = int(input())

graph = {i:[] for i in range(1, N+1)}
weight = {i:10**9 for i in range(N+1)}
for _ in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    
start, end = map(int, input().split())


# 1. 최소비용 출력 -> 다익스트라 
    # - 출발점과 도착점 주어져 있음 
    # - 버스비용 자연수 
    
def dijkstra(root):
    
    pq = [(0,root)]
    heapify(pq)
    weight[root] = 0 
    
    while pq:
        now_w, now_n = heappop(pq)

        # 얘를 빼서 시간 초과 났었음 ... ! -> 필요없는 코드는 없다 
        if now_w > weight[now_n]:
            continue
        
        for next_w, next_n in graph[now_n]:
            if next_w+now_w<weight[next_n]:
                weight[next_n]=next_w+now_w
                heappush(pq,(weight[next_n],next_n))


# 2. 실행 및 답 출력   
dijkstra(start)
print(weight[end])


