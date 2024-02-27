# 일방 통행 - 유방향 그래프 
# 사이클 이루는 도로의 길이의 합 최소 -> 최단 거리 
# 다시 시작점으로 돌아오기 -> 사이클 찾기 -> 유니온 파인드? -> 일단 보류 
# 거리는 자연수 
# 모든 노드 to 모든 노드 -> 확인해야 함 ㅇㅇㅇ -> 플로이드 워셜 v^3 = 20^3 = 
import sys
input = sys.stdin.readline

# 1. 입력 
V, E = map(int,input().split())
graph = [[10**9]*(V+1) for i in range(V+1)]

for _ in range(E): 
    a,b,c = map(int,input().split())
    graph[a][b]=c # (a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.

# 2. 플로이드 워셜 수행! 
for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] +graph[k][b]) 


# 3. 결과 출력 
min_road = 10**9
for a in range(1,V+1):
    for b in range(1,V+1):
        if a==b:
            min_road = min(graph[a][b], min_road)

if min_road==10**9:
    print(-1)
else:
    print(min_road)
