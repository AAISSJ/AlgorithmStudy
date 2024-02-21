# 연결하는 비용 최소 -> 최단 경로 or 최소 신장 트리 
    # 최단 경로 : 가중 그래프 상의 두 노드를 연결하는 가장 짧은 경로를 찾는 방법 / 방향&무방향
    # 최소 신장 트리 : 그래프 상의 모든 노드들을 최소 비용으로 연결하는 방법 / 무방향 only
# 본 문제에서는 모든 컴퓨터를 연결하는 데 필요한 최소 비용이므로 최소 신장 트리 
    # 크루스칼 또는 프림 알고리즘을 이용하면 되겠다 
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

arr = []
# # 1. 최단거리 정렬 
for _ in range(M):
    a,b,c = map(int, input().split()) # a컴퓨터와 b컴퓨터를 연결하는데 비용이 c
    arr.append((c,(a,b)))
    
arr.sort()

# 2. 하나씩 돌면서, 사이클이 되지 않은 경우(유니온 파인드)에 연결 
# 2-1.  배열 초기화 & 유니온 파인드 함수 추가 

parent = [i for i in range(N+1)]

def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b):
    a_root = find(a)
    b_root = find(b)
    parent[a_root]=b_root
    

# 2-2. 
answer = 0 
for edge in arr: 
    # 1) 하나 꺼내오기 
    weight, nodes = edge
    a, b = nodes
    # 2) 두 노드가 공통된 부모 갖는지 확인 -> 사이클 확인 
    if find(a)!=find(b):
        union(a,b)
        answer+=weight
    
print(answer)
        
   
    
    
    
    
