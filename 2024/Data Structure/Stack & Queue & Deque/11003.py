from collections import deque
import sys

input = sys.stdin.readline 

N, L = map(int, input().split())
arr = list(map(int, input().split()))

# arr = deque(arr)
dq = deque()

# 시간 초과남 
# for i in range(len(arr)): # O(N)
#     if i-L+1<0:
#         num = arr.popleft()
#         if min_num>num :
#             min_num=num
#         dq.append(num)
#         print(min(dq), end=' ')
#     else: 
#         num = arr.popleft()
#         if min_num>num :
#             min_num=num
#         dq.append(num)
#         print(min(dq), end=' ')
#         dq.popleft()


for i,n in enumerate(arr): # O(N)
    if i==0:
        dq.append((i,n))
    elif 1<=i<=L-1:
        while True:
            if len(dq)==0:
                break 
            if dq[-1][1] > n:
                dq.pop()
            else : 
                break
        dq.append((i,n))
    else:
        while True:
            if len(dq)==0:
                break 
            if dq[-1][1] > n:
                dq.pop()
            else : 
                break
        dq.append((i,n))
        if dq[0][0]<i-L+1:
            dq.popleft()
        
    print(dq[0][1], end=' ')    

        








