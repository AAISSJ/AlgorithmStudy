# 모든 노드가 연결되어 있나 아닌가 ? -> 사이클이 있나 없나 ? -> Union Find 
import sys
input = sys.stdin.readline 

N = int(input())
M = int(input())

# 1. 배열 초기화
parent = [i for i in range(N+1)]

# 2. Union Find 함수 구현  
def find(a):
    if parent[a]==a:
        return a 
    else : 
        parent[a] = find(parent[a])
        return parent[a]
        
def union(a,b):
    a_root = find(a)
    b_root = find(b)
    parent[a_root] =b_root
    
########################################################## 인덱스 조심! 1부터 시작해야 함 !
for i in range(1,N+1): 
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)+1): 
        if arr[j-1] :
            union(i,j)
          
# 3. 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별
path = list(map(int, input().split()))

root = find(path[0])
flag = 0 
for i in range(1, len(path)):
    if root != find(path[i]):
        flag=1
        break 

if flag: 
    print("NO")
else: 
    print("YES")
    
    
