from collections import deque 
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = {i+1:[] for i in range(N)}
visited = [0 for _ in range(N+1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

cnt = 1
def bfs(root):
    global cnt
    queue=deque([root])
    visited[root]=cnt
    while queue:
        current = queue.popleft()
        graph[current].sort()
        for next in graph[current]:
            if visited[next]==0:
                queue.append(next)
                cnt+=1
                visited[next]=cnt
    

bfs(R)

for i in range(N):
    print(visited[i+1])
