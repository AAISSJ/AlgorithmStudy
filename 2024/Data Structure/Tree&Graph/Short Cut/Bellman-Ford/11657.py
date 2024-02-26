# 가장 빠른 시간 구하기 -> 최단 경로 알고리즘 
    # 간선이 자연수가 아닌 경우 있음 -> 벨만 포드 알고리즘 

import sys 
input = sys.stdin.readline 

N,M = map(int, input().split())

# 모든 간선에 대한 정보를 담는 리스트 만들기 
edges = [] # <-> 그래프 만들지 않는다 like graph = {i:[] for in range(1,N+1)}
weight = [10**9 for i in range(N+1)]


for _ in range(M):
    A,B,C = map(int,input().split())
    edges.append((A,B,C))



def bellmanford(start):
    weight[start] = 0 
    
    # 전체 노드의 개수만큼,  
    for i in range(N): 
        # 모든 간선에 대해서, 간선을 지나는 경우 비용이 더 감소할 경우 업데이트
        for j in range(M): 
            now_n, next_n, cost = edges[j][0],edges[j][1],edges[j][2]
            if weight[now_n] !=10**9 and weight[next_n] >weight[now_n]+cost: 
                weight[next_n]=weight[now_n]+cost
                # 음수 순환 확인 : 맨 마지막 라운드에서도 값이 갱신되면 음수 순환이 존재한다는 것! 
                if i==N-1 : 
                    return True
    return False 

negative_cycle = bellmanford(1)

if negative_cycle: 
    print("-1")
else: 
    for i in range(2,N+1):
        if weight[i]==10**9: # 도달할 수 없는 경우 
            print("-1")
        else:
            print(weight[i])
    
