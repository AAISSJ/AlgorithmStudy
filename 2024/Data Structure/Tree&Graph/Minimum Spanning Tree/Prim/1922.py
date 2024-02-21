from heapq import *
import sys
input = sys.stdin.readline

def prim2(s):
    INF = 10001
    visited = [0] * (N + 1)     # MST에 포함된 노드들, 인덱스를 위해 (N+1)개
    weight = [INF] * (N + 1)    # 각 노드별 MST에 포함될 때의 소비한 가중치, 인덱스를 윌해 (N+1)개

    weight[s] = 0               # 시작노드는 가중치 0
    edges_heap = [(0, s)]       # 시작노드에 대한 정보를 heap에 넣어줘야 함 (가중치, 노드)
    heapify(edges_heap)         # heapify함수로 원래 list였던 edges_heap을 자료구조 heap으로 변경시켜줌

    while edges_heap:           # 힙이 소진될 때까지 반복
        mn, i_min = heappop(edges_heap) # python의 heapq는 최소힙으로, 항상 최소 가중치의 노드가 나옴
        if not visited[i_min]:          # 아직 MST에 포함되지 않은 인접 노드일 경우, 연산진행
            visited[i_min] = 1              # MST에 포함시킴
            for w, adj in adjLst[i_min]:    # 새로 MST에 추가된 노드에 대해서 인접 노드 가중치 최솟값으로 업데이트
                if not visited[adj] and weight[adj] > w:    # MST의 인접노드이며 & 최솟값일 경우 업데이트
                    weight[adj] = w
                    heappush(edges_heap, (w, adj))          # 해당 정보는 heap에 넣어줌 (가중치, 노드)

    print(sum(weight[1:]))

N = int(input())
M = int(input())

adjLst = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j, w = map(int, input().split())
    adjLst[i].append((w, j))
    adjLst[j].append((w, i))

prim2(1)
