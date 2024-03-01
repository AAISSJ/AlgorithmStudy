#  N개보다 많이 만드는 것도 N개를 만드는 것에 포함 -> 최대 랜선의 길이 -> upper bound 구하기

import sys 
input = sys.stdin.readline

# 0. 입력 받기 
K, N = map(int, input().split())
arr = []

for _ in range(K):
    arr.append(int(input()))
    
# 1. 이분 탐색 
start = 1  # 일반 이분탐색처럼 start를 0으로 설정하고 프로그램을 돌리면 런타임에러(ZeroDivisionError)가 발생한다
end = max(arr)

while start<=end: 
    mid = (start+end)//2
    
    # 만약 mid로 나눴을 때 N개만큼 나오는지 확인 
    cnt = 0 
    for num in arr: 
        cnt += num//mid 
    
    if N<=cnt: # 자른 결과가 N보다 같거나 더 크다면 -> 더 크게 자르기 
        start = mid+1
    else : # 자른 결과가 N보다 작으면 -> 더 작게 자르기 
        end = mid-1
        
        
print(end)    



# 맨 처음에 짠 코드 -> 반례 
# 4 4 
# 1
# 1
# 1
# 1
# import sys 
# input = sys.stdin.readline

# # 0. 입력 받기 
# K, N = map(int, input().split())
# arr = []

# for _ in range(K):
#     arr.append(int(input()))
    
# # 1. 이분 탐색 
# start = 0 
# end = 2**31-1

# while start<end: 
#     mid = (start+end)//2
    
#     # 만약 mid로 나눴을 때 N개만큼 나오는지 확인 
#     cnt = 0 
#     for num in arr: 
#         cnt += num//mid 
    
#     if N<=cnt:
#         start = mid+1
#     else : 
#         end = mid
        
        
# print(end-1)    
