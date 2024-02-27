# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램
# -> 플로이드 워셜 
import sys 
input = sys.stdin.readline 

# 0. 입력 받기 & graph 배열 초기화 
n = int(input())
m = int(input())
graph=[[10**9]*(n+1) for i in range(n+1)]

# 0-1. 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화 
for a in range(1, n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0 

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b]=min(c, graph[a][b]) # 노선이 하나가 아닐 수 있음 > 최소값 넣기
    
    
# 1. 점화식에 따라 플로이드 워셜 알고리즘 수행 
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+ graph[k][b])


# 2. 결과 출력 
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==10**9:
            print(0,end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
    
