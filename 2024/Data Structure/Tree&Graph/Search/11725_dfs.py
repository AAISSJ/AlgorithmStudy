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
