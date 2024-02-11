from collections import deque


N = int(input())
M = int(input())

graph={i+1:[] for i in range(N)}

for _ in range(M):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)


visited=[0 for i in range(N+1)]

def bfs(node):
  queue = deque([node])
  visited[node]=1
  while queue:
    current = queue.popleft()
    for next in graph[current]:
      if visited[next]==0:
        visited[next]=1
        queue.append(next)

bfs(1)

print(sum(visited)-1)
