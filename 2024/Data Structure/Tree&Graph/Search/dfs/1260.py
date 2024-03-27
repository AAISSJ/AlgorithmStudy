import sys 
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = {i+1:[] for i in range(N)}

for _ in range(M):
    node1, node2= map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited_dfs={i+1:-1 for i in range(N)}
check_dfs=[]

cnt=1
def dfs(root):
    global cnt 
    global check_dfs
    visited_dfs[root]=cnt
    check_dfs.append(root)
    graph[root].sort()
    for node in graph[root]:
        if visited_dfs[node]==-1:
            cnt+=1
            check_dfs.append(node)
            visited_dfs[node]=cnt
            dfs(node)

dfs(V)


# BFS
visited_bfs={i+1:-1 for i in range(N)}
check_bfs=[]

cnt =1 
def bfs(root):
    global cnt 
    global check_bfs
    visited_bfs[root]=cnt 
    queue=deque([root])
    check_bfs.append(root)
    while queue:
        current = queue.popleft()
        check_bfs.append(current)
        graph[current].sort()
        for next in graph[current]:
            if visited_bfs[next]==-1:
                check_bfs.append(next)
                queue.append(next)
                cnt+=1
                visited_bfs[next]=cnt 

bfs(V)


for index, order in sorted(visited_dfs.items(), key=lambda x:x[1]):
    if order!=-1:
        print(index, end=' ')

print('')

for index, order in sorted(visited_bfs.items(), key=lambda x:x[1]):
    if order!=-1:
        print(index, end=' ')

