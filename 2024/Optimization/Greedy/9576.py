import sys 
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    apply_arr = []
    dic = {i:0 for i in range(1,N+1)}
    for _ in range(M):
        apply_arr.append(list(map(int,input().split())))

    sorted_arr = deque(sorted(apply_arr, key=lambda x:x[1]))
    cnt = 0 
    
    while sorted_arr : 
        start_index, end_index = sorted_arr.popleft()
        for i in range(start_index, end_index+1):
            if dic[i]==0:
                dic[i]=1
                cnt+=1 
                break 
    print(cnt)
