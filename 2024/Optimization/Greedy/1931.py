import sys 
from collections import deque 
input = sys.stdin.readline 


# 0. 입력 
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 1. Greedy - 매번 종료 시간을 기준으로 가장 빠른 애 택하기 

sorted_arr = deque(sorted(arr, key=lambda x:(x[1],x[0])))
cnt = 1
start_time, end_time = sorted_arr[0][0],  sorted_arr[0][1]
sorted_arr.popleft()
while sorted_arr:
    
    if end_time<=sorted_arr[0][0]:
        cnt+=1 
        new = sorted_arr.popleft()
        start_time, end_time = new[0], new[1]
    else: 
        sorted_arr.popleft()
    
print(cnt)

