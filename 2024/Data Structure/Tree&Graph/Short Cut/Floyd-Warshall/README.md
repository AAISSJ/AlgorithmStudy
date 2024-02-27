# Floyd Warshall 
## 1. 개념 및 기본 원리 
-  Floyd Warshall 알고리즘은 **모든 정점에서 다른 모든 정점으로의 최단 경로**를 구하는 알고리즘
-  다이나믹 프로그래밍 유형에 속함
  - 점화식에 맞게 삼중 for문 수행 
- 기본 원리 : 각 단계마다 특정한 노드 K를 거쳐가는 경우를 확인 
  - a에서 b로 가는 최단 거리보다 a에서 k로 거쳐 b로 가는 거리가 더 짧은지 검사 

![image](https://github.com/AAISSJ/AlgorithmStudy/assets/76966915/56905997-b486-4833-be3d-22fcfad0da41)


## 2. 시간 복잡도 
- Floyd Warshall의 시간 복잡도는 O(v^3)
  - 노드의 수가 적을 때 사용 가능 


## 3. 사용 조건 



## 4. 사용되는 자료구조 및 알고리즘 & 기본 코드
```python
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램
# -> 플로이드 워셜 
import sys 
input = sys.stdin.readline 

# 0. 입력 받기 & graph 배열 초기화 
n = int(input())
m = int(input())
graph=[[10**9]*(n+1) for i in range(n+1)]

# 0-1. 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화 
for a in range(1, n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0 

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b]=c
    
    
# 1. 점화식에 따라 플로이드 워셜 알고리즘 수행 
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+ graph[k][b])


# 2. 결과 출력 
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==10**9:
            print(0,end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
    

```


## 5. 문제 유형 


## 6. 다른 알고리즘과의 차이점 
- 다익스트라와의 차이점
  - Dijkstra 알고리즘은 하나의 정점에서 출발했을 때 다른 모든 정점으로의 최단 경로를 구하는 알고리즘

