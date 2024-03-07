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
            # dp배열 비교후 힙큐에 넣는 부분 파트를 1차관문이라고 본다면, 힙큐에서 pop을 해주고 dp배열을 비교해주는 것을 2차관문이라고 비유해 보겠습니다. 
            # 예를 들어서 여러 간선을 통해서  [정점,(누적)비용 ] =  (E,1)  ,(E , 2) , (E,3) , (E,4) , (E,5) 을 순차적으로 1차관문에서 테스트를 한다면, 
            # 1차 관문에서 dp[E] =1로 최소비용이 설정이 되고, 나머지 2,3,4,5, 는 최소비용보다 크므로, 힙에 들어가지 못합니다. 
            # 하지만,  [정점,(누적)비용 ] = (E , 5) , (E,4) , (E,3) , (E,2) , (E,1) 순으로 순차적으로 1차관문에서 테스트를 한다면, 
            # 1차 관문에서 dp[E] = 5 => dp[E] = 4 -> dp[E] =3 .... 순으로 계속 업데이트가 되면서, 위의 (정점,비용) 케이스가 전부 힙에 들어가게 됩니다. 
            # 그렇다면, 2차 관문이 없다라면, 비록 힙큐에서 pop을  (E,1) 부터 해주지만, 2차관문에서 걸려주는 역할이 없기 때문에, (E,1 ~5) 까지 계속 연결된 간선을 확인하는 과정을 거치게 돼 시간초과가 발생합니다
        if now_w > weight[now_n]:
            continue
        
        for next_w, next_n in graph[now_n]:
            if next_w+now_w<weight[next_n]:
                weight[next_n]=next_w+now_w
                heappush(pq,(weight[next_n],next_n))


# 2. 실행 및 답 출력   
dijkstra(start)
print(weight[end])


