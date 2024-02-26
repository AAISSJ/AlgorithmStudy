# 이 문제는 논란거리가 많단다 https://www.acmicpc.net/board/view/72995
# 백준이가 시간이 줄어들면서, 출발 위치로 돌아오는 것이 가능한지를 물어보기 때문에, 
# 우리는 주어진 그래프에서 벨만-포드 알고리즘이 무한히 반복되는 경우 (음수 사이클에 빠지는 경우)를 찾아야 한다.

import sys 
input = sys.stdin.readline 


def bellmanford(start):
    weight[start] = 0 
    for i in range(N):
        for j in range(2*M+W):
            now_n, next_n, cost = edges[j][0], edges[j][1], edges[j][2]
            if weight[next_n]>weight[now_n]+cost: #  weight[now_n]!=10**9 and <- 이거 검사 안하는 게 이 문제의 핵심이다! 
                weight[next_n]=weight[now_n]+cost
                if i==N-1:
                # 노드의 갯수가 N개라고 하면, 벨만 포드 알고리즘은 N-1번의 순환 이내에 최적화된 경로를 반드시 뱉어낸다. 
                # 그렇다면, 알고리즘이 N-1번을 넘어 N번째의 순환에 돌입한다면, 이건 뭔가 하자가 있는 (음수 사이클이 있는) 케이스라고 생각할 수 있다
                    return True
    return False 
            
            
tc= int(input())

for _ in range(tc):
    N,M,W = map(int, input().split())
    
    edges = []
    weight = [10**9 for i in range(N+1)] 
    for _ in range(M):
        S,E,T = map(int,input().split())
        edges.append((S,E,T))
        edges.append((E,S,T))
        
    for _ in range(W):
        S,E,T = map(int,input().split())
        edges.append((S,E,-T))

    negative_cycle = bellmanford(1)
    if negative_cycle:
        print("YES")
    else: 
        print("NO")

            
        
    
    
    
