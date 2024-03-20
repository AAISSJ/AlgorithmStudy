import sys 

input = sys.stdin.readline 


# 플로이드-와샬 
# all - all -> n^3 
# 각 단계마다 특정한 노드 K를 거쳐가는 경우를 확인
# a에서 b로 가는 최단 거리보다 a에서 k로 거쳐 b로 가는 거리가 더 짧은지 검사


# 0. 입력 받기 
n = int(input())
m = int(input())

graph = [[10**9]*(n+1) for i in range(n+1)]
path = [[0]*(n+1) for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    if c<graph[a][b]:
        graph[a][b]=c
        path[a][b]=[a,b]

# 1. 플로이드-와샬
## 1-1. 자기 자신으로 가는 경우 0으로 초기화 
for a in range(1,n+1):
    graph[a][a]=0
    path[a][a]=[a]

## 1-2. 점화식 수행 
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            current = graph[a][b]
            graph[a][b]=min(graph[a][k]+graph[k][b], graph[a][b])
            if current != graph[a][b]:
                path[a][b]=path[a][k]+path[k][b][1:]

            
# 2. 출력 
## 2-1. 최소비용 
for a in range(1, n+1):
    for b in range(1,n+1):
        if graph[a][b]==10**9:
            print(0,end=' ')
        else:
            print(graph[a][b],end=' ')
    print()

        

## 2-2. 최소 비용에 포함되어 있는 도시의 개수 k + 도시 i에서 도시 j로 가는 경로
for a in range(1, n+1):
    for b in range(1,n+1):
        if graph[a][b]==10**9 or graph[a][b]==0:
            print(0)
        else:
            print(len(path[a][b]),end=' ')
            print(' '.join(map(str,path[a][b])))
        
