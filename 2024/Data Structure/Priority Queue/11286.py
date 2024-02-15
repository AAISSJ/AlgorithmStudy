import sys 
import heapq
input= sys.stdin.readline

N = int(input())
arr = []
heapq.heapify(arr)


for _ in range(N):
    num = int(input())
    if num ==0 :
        if len(arr)>=2:
            tmp1 = heapq.heappop(arr)
            tmp2 = heapq.heappop(arr)
            if tmp1[0] < tmp2[0]: 
                print(tmp1[1])
                heapq.heappush(arr, tmp2)
            elif tmp1[0] == tmp2[0]: 
                if tmp1[1]> tmp2[1]:
                    print(tmp2[1])
                    heapq.heappush(arr, tmp1)
                else: 
                    print(tmp1[1])
                    heapq.heappush(arr, tmp2)
        elif len(arr)==1: 
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    elif num<0:
        heapq.heappush(arr, (-num, num))
    else: 
        heapq.heappush(arr, (num, num))
        
        
