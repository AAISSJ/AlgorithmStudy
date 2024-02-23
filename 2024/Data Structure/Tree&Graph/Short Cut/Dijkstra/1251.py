import sys 
from heapq import * 

input = sys.stdin.readline 
M, N = map(int, input().split())

check = [[1,0],[0,1],[-1,0],[0,-1]]
graph = [[]]
weight = [[]]

for _ in range(N):
    row = list(input().rstrip())
    graph.append([0]+row)
    weight.append([10**10 for i in range(len(row)+1)])

def dijkstra(root):
    weight[root[0]][root[1]] = 0
    pq = [(weight[root[0]][root[1]],root)]
    heapify(pq)
    while pq:
        now = heappop(pq)
        now_w, now_x, now_y = now[0], now[1][0], now[1][1]
        # print("now",now_x, now_y)
        # print("now weight",now_w)

        for dx,dy in check: 
            next_x, next_y = now_x+dx, now_y+dy
            if 1<=next_x<=N and 1<=next_y<=M : 
                # print("next", next_x, next_y)
                if weight[next_x][next_y]>weight[now_x][now_y]+int(graph[next_x][next_y]):
                    weight[next_x][next_y] = weight[now_x][now_y]+int(graph[next_x][next_y])
                    next_w = weight[next_x][next_y]
                    # print("next weight",next_w)
                    heappush(pq, (next_w,(next_x, next_y)))


dijkstra((1,1))

# print(weight)
print(weight[N][M])
