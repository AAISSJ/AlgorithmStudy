
# BFS & DFS

## BFS
### 1. 개념 및 기본 원리 


### 2. 시간 복잡도 

### 3. 사용 조건 

### 4. 사용되는 자료 구조 및 알고리즘 & 기본 코드 
- queue를 사용한다

```python
from collections import deque
import sys 

input = sys.stdin.readline


N=int(input())
graph = {i+1: [] for i in range(N)}

for i in range(N-1):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1) 


visited = [0 for i in range(N+1)]

def bfs(node):
  queue = deque([node])
  while queue:
    current = queue.popleft()
    for i in graph[current]:
      if visited[i]==0:
        visited[i]=current
        queue.append(i)

bfs(1)

for i in range(2, N+1):
  print(visited[i])
```

### 5. 문제 유형

<br>

## DFS
### 1. 개념 및 기본 원리 


### 2. 시간 복잡도 

### 3. 사용 조건 

### 4. 사용되는 자료 구조 및 알고리즘 & 기본 코드 
- 재귀를 사용한다 
```python
from collections import deque
import sys 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


N=int(input())
graph = {i+1: [] for i in range(N)}

for i in range(N-1):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1) 

visited = [0 for i in range(N+1)]

def dfs(node):
  for next in graph[node]:
    if visited[next]==0: # 아직 방문을 안했다면 
      visited[next]=node
      dfs(next)

dfs(1)

for i in range(2, N+1):
  print(visited[i])
```


### 5. 문제 유형
