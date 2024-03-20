import sys 
from collections import deque 
input = sys.stdin.readline


n,m = map(int,input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))
    
check = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs(x,y):
    queue = deque([(x,y)])
    cnt = 0 
    while queue:
        now_x, now_y = queue.popleft()
        if arr[now_x][now_y]:
            arr[now_x][now_y]=0
            cnt+=1
            for dx,dy in check:
                next_x, next_y = now_x+dx, now_y+dy
                if 0<=next_x<n and 0<=next_y<m and arr[next_x][next_y]:
                    queue.append((next_x,next_y))
    return cnt 
    
max_pic = 0 
pic_cnt = 0 

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            tmp = bfs(i,j)
            pic_cnt+=1
            if tmp > max_pic:
                max_pic=tmp 
print(pic_cnt)
print(max_pic)
        
