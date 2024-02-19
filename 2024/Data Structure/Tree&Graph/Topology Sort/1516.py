from collections import deque 
import sys 

input = sys.stdin.readline 

N = int(input())

in_degree = [ 0 for i in range(N+1)]
graph = [[] for i in range(N+1)]
time =  [0 for i in range(N+1)]


# 초기화 
for i in range(1, N+1):
    line = list(map(int, input().split()))
    # 시간 넣기 
    time[i]=line[0]
    # 연결시키기 
    for j in range(1,len(line)-1):
        graph[line[j]].append(i) # line[j]는 선행되어야 하는 건물들, i는 현재 건물
        in_degree[i] += 1 # 현재 건물 i로 들어오는 진입 차수 올려주기        
    # print(graph)


# # 위상 정렬 
def topo_sort():
    queue = deque()    
    result = [0 for i in range(N+1)]
    # 1. 진입 차수 0인 애들부터  
    for i in range(N+1):
        if in_degree[i]==0:
            queue.append(i)

    while queue:
        now = queue.pop()
        result[now]+=time[now]
        for i in graph[now]:
            in_degree[i]-=1
            result[i] = max(result[i], result[now])
            if in_degree[i] ==0 :
                queue.append(i) 
    return result
    

result = topo_sort()

for i in range(1,N+1):
    print(result[i])
