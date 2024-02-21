import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, R = map(int, input().split())


graph = {i+1:[] for i in range(N)}
visited = [0 for _ in range(N+1)]

for _ in range(M):
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

cnt=1

def dfs(current):
  global cnt 
  visited[current]=cnt
  graph[current].sort()
  for next in graph[current]:
    if visited[next]==0:
      cnt+=1
      dfs(next)

dfs(R)

for i in range(1, N+1):
  print(visited[i])
