# Bellman Ford
## 1. 개념 및 기본 원리 
- 다익스트라와 달리, 음수 간선이 있는 경우
  - 음수 간선 순환이 없는 경우
  - 음수 간선 순환이 있는 경우
    - 아래 그림과 같이 무한히 값이 작아지는 문제 발생 => 벨만 포드 알고리즘은 이를 해결할 수 있음! 
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/98540d3c-ef5a-48f0-86be-7b339c20f605)

- 벨만 포드는 음의 간선이 포함된 상황에서도 사용될 수 있으며, 음수 간선의 순환을 감지할 수 있음 

<br>

## 2. 시간 복잡도
- 벨만 포드의 시간 복잡도는 o(VE)
  - 다익스트라 알고리즘에 비해 느림 

<br>

## 3. 사용 조건
- 다익스트라와 달리, 음수 간선이 있는 경우

<br>

## 4. 사용되는 자료구조 및 알고리즘 & 기본 코드
```
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
```
<br>

## 5. 문제 유형

<br>

## 6. 다른 알고리즘과의 차이점 
- 벨만 포드 알고리즘 <-> 다익스트라 
  - 벨만 포드
    - 전체 간선 E를 확인한다
    - 음수 간선의 순환을 체크하기 위해 전체 간선을 하나씩 확인하여 갱신하는 과정을 한 번 더 거치게 된다 
  - 다익스트라
    - 현재 노드와 인접한 간선만을 탐색한다 
