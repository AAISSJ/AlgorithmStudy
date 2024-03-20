# Kruskal 알고리즘 

## 1. 개념 및 기본 원리 

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/e9c44b34-6ad8-4d58-8a1c-046095e64679)


1. 그래프의 간선들을 **가중치의 오름차순으로 정렬**한다.
2. 정렬된 간선 리스트에서 순서대로 **사이클을 형성하지 않는 간선을 선택**한다.
    - 즉, **가장 낮은 가중치를 먼저 선택**한다.
    - 사이클을 형성하는 간선을 제외한다.
![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/3955ab7c-6a04-4b25-aa2f-1d6d81abc618)
  

3. 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.



<br>

## 2. 시간 복잡도 
- 크루스칼 알고리즘의 시간 복잡도는 **Elog(E)**
  - 시간이 가장 오래 걸리는 부분이 **간선을 정렬하는 작업**이며, E개의 데이터를 정렬했을 때의 시간 복잡도는 O(ElogE)이기 때문
  - 내부에서 동작하는 Union Find 알고리즘의 시간 복잡도는 이보다 작으므로 무시함 

<br>

## 3. 사용 조건 
- 프림은 정점 위주의 알고리즘, 크루스칼은 간선 위주의 알고리즘
  - 프림의 경우 최소 거리의 정점을 찾는 부분에서 자료구조의 성능에 영향을 받는다.
  - 크루스칼은 간선을 기준으로 정렬하는 과정이 오래 걸린다.
- 간선의 개수가 작은 경우에는 크루스칼, 간선의 개수가 많은 경우에는 프림.



<br>

## 4. 사용되는 자료구조 및 알고리즘 & 기본 코드
```python
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
```

## 5. 문제 유형 
