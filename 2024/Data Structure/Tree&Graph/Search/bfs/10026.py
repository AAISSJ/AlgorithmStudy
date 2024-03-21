import sys 
from collections import deque 
input = sys.stdin.readline
N = int(input())

check = [[1,0],[-1,0],[0,1],[0,-1]]
arr = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    tmp = list(input().rstrip('\n'))
    arr.append(tmp)

def bfs(pair,color):
    queue = deque([pair])
    visited[pair[0]][pair[1]] = 1
    while queue: 
        now_x, now_y = queue.popleft()
        for dx,dy in check:
            next_x, next_y = now_x+dx, now_y+dy
            if 0<=next_x<N and 0<=next_y<N and arr[next_x][next_y] in color and not visited[next_x][next_y]:
                visited[next_x][next_y]=1
                queue.append((next_x,next_y))
  
 
# 1. 적록색약이 아닌 사람이 보는 구역 수                   
cnt = 0
for a in range(N):
    for b in range(N):
        if not visited[a][b]:
            cnt += 1
            bfs((a,b),arr[a][b])
            
# 2. 적록색약이 보는 영역 
cnt_rgb = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for a in range(N):
    for b in range(N):
        if not visited[a][b]:
            if arr[a][b] in 'RG':
                bfs((a,b),'RG')
            else:
                bfs((a,b),'B')
            cnt_rgb+=1
            
print(cnt, cnt_rgb)
    
