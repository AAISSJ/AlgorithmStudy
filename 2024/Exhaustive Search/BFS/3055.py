from collections import deque
import sys 

input = sys.stdin.readline


R,C = map(int, input().split())

# 최소 시간 - 최단 거리 - Bfs ?? 
# 물도 매 분마다 비어있는 칸으로 확장한다 -> 물 bfs 
# 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다 -> 고슴도치 bfs
# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다 -> 물 bfs  먼저 


# 1. map 입력 받기 & S(고슴도치)의 위치 파악 & 물 위치 파악 
check = [[0,1],[1,0],[-1,0],[0,-1]]
map_list = []
visited = []
water_queue = deque([])
s_queue = deque([])

# 맨 처음 queue값 세팅 
for i in range(R):
    string = input()
    map_list.append(list(string))
    visited.append([0]*len(string))
    for j in range(len(string)):
        if string[j]=='S':
            s_queue.append([i,j])
        if string[j]=='*':
            water_queue.append([i,j])


cnt = 0

def bfs(): 
    global cnt 
    
    while True: # 1회당 
        cnt+=1
        
        len_s = len(s_queue)
        len_water = len(water_queue)
        if not s_queue:
            cnt = None
            break
        
        # 물 bfs
        while len_water>0: # while water_queue 아님 
            len_water -=1
            x,y= water_queue.popleft()
            for dx, dy in check:
                if 0<=x+dx<R and 0<=y+dy<C and map_list[x+dx][y+dy]=='.':
                    water_queue.append([x+dx,y+dy])
                    map_list[x+dx][y+dy]='*'
        while len_s>0: # while s_queue 아님
            len_s-=1
            x,y=s_queue.popleft()
            for dx,dy in check: 
                if 0<=x+dx<R and 0<=y+dy<C:
                    if map_list[x+dx][y+dy]=='D':
                        return
                    if  map_list[x+dx][y+dy]=='.' : # and visited[x+dx][y+dy]==0
                        s_queue.append([x+dx,y+dy])
                        map_list[x+dx][y+dy]='S'
bfs()

if cnt:
    print(cnt)
else:
    print('KAKTUS')

    
