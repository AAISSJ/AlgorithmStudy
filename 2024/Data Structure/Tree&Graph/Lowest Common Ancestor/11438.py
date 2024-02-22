import sys
input = sys.stdin.readline # 시간 초과를 피하기 위한 빠른 입력 함수
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정


# 0. 입력 받기 및 필요한 배열 선정
LOG = 21 # 2^20 = 1,000,000

n = int(input()) # 노드의 개수 
parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프(graph) 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    
# 1. 각 노드의 깊이 구하기 & 부모 노드 구하기 by dfs 
# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y][0] = x # 부모 노드 구하기 
        dfs(y, depth + 1)

dfs(1, 0) # 루트 노드는 1번 노드
# print(d)


# 2. 부모(i=0)보다 높은 전체 조상(1<=i<LOG) 관계를 설정하는 함수
def set_parent():
    for i in range(1, LOG):
        for j in range(1, n + 1): # 루트 노드 빼고 
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


set_parent()
# print(parent)

# 3. A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    
    # 1) 항상 b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
            
    # 2) a와 b의 깊이가 동일해주도록 설정
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= 2**i:
            b = parent[b][i]
            
            
    # 3-1) 깊이가 같을 때 둘이 동일하다면? ( 11438번 문제의 예제 1의 2,6의 경우 ) 
    if a == b:
        return a
    
    # 3-2) (깊이가 같지만 둘이 동일하지 않은 경우) 위로 올라가면서 공통 조상 찾기
    for i in range(LOG - 1, -1, -1): # 
        # 위(루트)를 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]: # a와 b의 부모가 같아지면 갱신하지 않음
            # ( 11438번 문제의 예제 1의 8,15의 경우 ) 
            a = parent[a][i]
            b = parent[b][i]
        
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]


# Test Case 입력
m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
    
