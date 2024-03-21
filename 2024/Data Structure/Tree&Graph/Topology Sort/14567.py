import sys 
from collections import deque
input = sys.stdin.readline 


N,M = map(int,input().split())

arr = {i:[] for i in range(1,N+1)}
in_degree = [0 for i in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    # init - A(선수)-> B(후수)
    arr[A].append(B)
    in_degree[B]+=1

def topological_sort():
    
    queue = deque([])
    result = []
    for i in range(1,N+1):
        if in_degree[i]==0:
            queue.append((i,1))
            
    while queue: 
        now_n,now_semester = queue.popleft()
        result.append((now_n,now_semester))
        
        for next_n in arr[now_n]:
            in_degree[next_n]-=1
            if in_degree[next_n]==0:
                queue.append((next_n,now_semester+1))
                
    return result 
    
result=topological_sort()

sorted_result = sorted(result, key=lambda x:x[0])
for class_name, semester in sorted_result:
    print(semester, end=' ')
