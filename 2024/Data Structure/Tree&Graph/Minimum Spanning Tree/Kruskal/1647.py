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
edges = []
for _ in range(M):
    A,B,C = map(int, input().split())
    edges.append((C,A,B))

edges.sort()


arr = [i for i in range(N+1)]

def union(a,b):
    a_root = find(a)
    b_root = find(b)
    arr[a_root]=b_root
    
def find(a):
    if arr[a]==a:
        return a 
    else : 
        arr[a]=find(arr[a])
        return arr[a]


cost = 0 
max_c = 0 
for c, a, b in edges:
    if find(a)!=find(b):
        union(a,b)
        cost += c
        if max_c < c :
            max_c = c

print(cost-max_c)


