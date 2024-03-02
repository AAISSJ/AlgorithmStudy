import sys
from heapq import *
input = sys.stdin.readline

N, K = map(int,input().split())
graph = [10**9 for i in range(10**5+1)]

# 가장 빠른 시간 출력 -> 최단 거리 
# 움직이는 방법마다 가중치 다름 -> 다익스트라 
# 다익스트라 특징 
# 1. 우선 순위 큐 
# 2. 중복 체크 안 함 
# 3. weight 배열에 간 거리 기록하고, 현재 배열 값보다 더 작아지면 갱신 


def dijkstra():
    pq = [(0,N)]
    heapify(pq)
    cnt = 0 
    graph[N]=0
    while pq: 
        now_weight, now_n = heappop(pq)
        if now_n==K:
            print(graph[K])
            break 
        check = [(1, now_n-1), (1, now_n+1),(0,now_n*2)]
        for weight,next_n in check: 
            if 0<=next_n<=10**5:
        
                if weight+now_weight<graph[next_n]:
                    graph[next_n]= now_weight+weight
                    heappush(pq, (graph[next_n], next_n))
    

dijkstra()
