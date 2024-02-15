import heapq 
import sys 

input = sys.stdin.readline

N = int(input())

arr = []
heapq.heapify(arr)


for _ in range(N):
    num = int(input())
    if num == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else: 
        heapq.heappush(arr, num)
        

    
