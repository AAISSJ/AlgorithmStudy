import sys 
from collections import deque
input = sys.stdin.readline 

N, M = map(int, input().split())

graph = [[]]
visited = [[]] 
check = [[1,0],[0,1],[-1,0],[0,-1]]

for i in range(N):
    row=list(input().rstrip())
    graph.append([0]+row)
    visited.append([0]+[0 for i in range(len(row))])


def bfs(root):
    queue = deque([root])
    visited[root[0]][root[1]]=1
    while queue:
        now_x, now_y = queue.popleft()
        for dx,dy in check : 
            next_x,next_y= now_x+dx, now_y+dy
            if 1<=next_x<=N and 1<=next_y<=M :
                if graph[next_x][next_y]=='1':
                    if not visited[next_x][next_y]:
                        queue.append([next_x,next_y])
                        visited[next_x][next_y] = visited[now_x][now_y]+1

        
bfs([1,1])
print(visited[N][M])

# import sys 
# from collections import deque
# input = sys.stdin.readline 

# N, M = map(int, input().split())

# graph = [[]]
# check = [[1,0],[0,1],[-1,0],[0,-1]]

# for i in range(N):
#     row=list(input().rstrip())
#     graph.append([0]+row)
    
# def bfs(root):
#     queue = deque([root])
#     while queue:
#         now_x, now_y = queue.popleft()
#         for dx,dy in check : 
#             next_x,next_y= now_x+dx, now_y+dy
#             if 1<=next_x<=N and 1<=next_y<=M :
#                 if graph[next_x][next_y]=='1':
#                     queue.append([next_x,next_y])
#                     graph[next_x][next_y]=int(graph[now_x][now_y])+1

# bfs([1,1])
# print(graph[N][M])
