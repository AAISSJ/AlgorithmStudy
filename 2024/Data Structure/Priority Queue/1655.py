# 이 문제의 어딜 보고 우선 순위 큐 활용 문제임을 알 수 있을까? 

import sys 
import heapq 
input = sys.stdin.readline 

N = int(input())

arr = [] 
heapq.heapify(arr)

# 0. 힙큐 left, right 두 개 쓰기 ??  


# 1.  O(N^2)... 어떻게 더 효율적으로 풀지 
# for i in range(N):
#     num = int(input())
#     heapq.heappush(arr, num)
#     len_arr =  len(arr)
#     if len_arr%2 == 0 : 
#         tmp = []
#         for _ in range(len_arr//2): 
#             tmp.append(heapq.heappop(arr))
#         print(tmp[-1])
#         for i in range(len_arr//2): 
#             heapq.heappush(arr, tmp[i])                
#     else : 
#         tmp = []
#         for _ in range(len_arr//2+1): 
#             tmp.append(heapq.heappop(arr))
#         print(tmp[-1])
#         for i in range(len_arr//2+1): 
#             heapq.heappush(arr, tmp[i])                


# 2. 답 확인 - 힙큐 두 개 쓰는 게 맞다 ...



# 정렬이 필요 -> Priority Queue로 어떻게 하나?!
# -> left [max_heap] //right [min_heap] - 두 개 써보자 
    # 수가 짝수 개면 작은 수 골라라 
    # max_heap 우선 채우고, max_heap peek하기 
    # 단, max_heap에는 min_heap보다 작은 수만 존재하도록 


# 왼쪽 힙은 최대 힙으로 정렬하고, 오른쪽 힙은 최소 힙으로 정렬하면
# 왼쪽 힙의 첫번째 요소는 항상 중앙값이 된다.

# 이때 왼쪽 힙의 첫번째 요소는 최대 힙에서 가장 큰 값이다.
# 마찬가지로 오른쪽 힙의 첫번째 요소는 최소 힙에서 가장 작은 값


min_heap = [] 
max_heap = []
heapq.heapify(min_heap)
heapq.heapify(max_heap)

for i in range(N):
    x = int(input())
    
    if len(min_heap)==len(max_heap): # 크기 같을 때 max_heap 우선 채우고
        heapq.heappush(max_heap, -x)
    else: 
        heapq.heappush(min_heap, x) 
        
        
    if max_heap and min_heap:
        if - max_heap[0]> min_heap[0] : 
            tmp = - heapq.heappop(max_heap)
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, tmp)
    
    print(-max_heap[0])
        
        
        

