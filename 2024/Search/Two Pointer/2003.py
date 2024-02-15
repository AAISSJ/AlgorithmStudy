import sys 

input = sys.stdin.readline

N,M = map(int, input().split())
arr = list(map(int, input().split()))

# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우
# 연속된 부분 배열 - two pointer 
# 1. 정렬 X -> 둘다 왼쪽에서 시작 


cnt =0 
left =0 
right = 0 
sum_num = 0 


# while right< N : 
#     sum_num = sum(arr[left: right+1])
#     if sum_num==M : 
#         cnt+=1
#         right +=1
#     elif sum_num> M : 
#         left+=1
#     else: 
#         right+=1 

while True: 
    if right >= N  : # 만약 끝까지 도달한다면  ## or left>right
        break 
    sum_num= sum(arr[left:right+1])
    if sum_num==M : 
        cnt+=1
        right +=1
    elif sum_num> M : 
        left+=1
    else: 
        right+=1 

print(cnt)

# 맨처음에 30줄에 있는 조건에 or left>right를 넣어서 틀렸는데 
# 항상 left가 right보다 작아야 하지 않나? 생각했음 
# 반례 찾음 
# [1,2,4,3]에서 합이 3이 되는 부분 배열 찾기 
# left = 2, right =2 인 상황에서 합이 4가 되고, 그보다 값이 작아야 하니까 left가 커짐 
# 따라서 left = 3, right=2가 됨 이렇게 되면 arr[left:right+1]은 []값을 갖게 된다 
# 다음 차례엔 무조건 right가 커지게 된다
# 그럼 이럴 때 중복되게 세어지는 경우는 없는 건가 ???





