import sys 
from collections import deque
input = sys.stdin.readline 

N, K = map(int, input().split())

graph = [0 for i in range(10**5+1)]


def bfs():
    queue = deque()             
    queue.append(N)             
    while queue:
        x = queue.popleft()     
        if x == K:
            print(graph[x])
            break
        for nx in (x - 1, x + 1, x * 2):    
            if 0 <= nx <= 10**5 and not graph[nx]:
                graph[nx] = graph[x] + 1
                queue.append(nx)    

bfs()
