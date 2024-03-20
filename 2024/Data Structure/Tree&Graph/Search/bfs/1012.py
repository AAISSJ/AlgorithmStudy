# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 
# bfs 
import sys
from collections import deque 
input =sys.stdin.readline

T = int(input())
check = [[1,0],[0,1],[-1,0],[0,-1]]
for _ in range(T):
    # 0. 입력 받기 
    M, N, K = map(int,input().split())
    arr = []
    graph = [[0]*N for i in range(M)]
    for _ in range(K):
        x,y = map(int,input().split())
        graph[x][y] = 1
        arr.append((x,y))
    
    # 1. bfs 돌며 땅 찾기
    cnt = 0 
    for x,y in arr: 
        if graph[x][y]==1:
            cnt+=1
            queue = deque([(x,y)])
            while queue: 
                now = queue.popleft()
                now_x, now_y = now[0], now[1]
                graph[now_x][now_y] = 0 
                for dx,dy in check:
                    next_x, next_y = now_x+dx, now_y+dy
                    if 0<=next_x<M and 0<=next_y<N and graph[next_x][next_y]: 
                        queue.append((next_x,next_y))
                        graph[next_x][next_y] = 0 
    print(cnt)
