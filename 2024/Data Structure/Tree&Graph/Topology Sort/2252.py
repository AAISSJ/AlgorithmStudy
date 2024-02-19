
from collections import deque 
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())

arr = [[] for i in range(N+1)]
in_degree = [0 for i in range(N+1)] # 진입차수


def init(a,b):
    arr[a].append(b) # A가 선행, B가 후행 
    in_degree[b]+=1 # A의 선수로 B가 지정되었으므로 진입차수를 1 추가


# init
for _ in range(M):
    A,B =  map(int, input().split())
    init(A,B)
    
# print(arr)
# print(in_degree)

# topology sort
def topology_sort():
    result = [] 
    queue = deque()
    # 처음 시작할 떄는 진입 차수가 0인 노드를 먼저 큐에 넣기 
    for i in range(1, N+1):
        if in_degree[i]==0 : # 진입차수가 0이라면 == 리프노드라면 
            queue.append(i)
    
    # 큐가 빌 때까지 
    while queue:
        now = queue.popleft()
        result.append(now)
        print(now, end=' ')
        
        for next_one in arr[now]:
            in_degree[next_one]-=1
            if in_degree[next_one] == 0 : # 새롭게 진입차수가 0이 되는 노드들을 삽입
                queue.append(next_one)

topology_sort()
                
