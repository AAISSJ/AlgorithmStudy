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
