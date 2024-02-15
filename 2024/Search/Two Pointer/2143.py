# 이 문제는 세 가지 방법으로 풀 수 있다 
# 1. two pointer, 2. binary search, 3. hash 
# 맨 처음에 two pointer로 시도해본 코드 다시 도전해보자

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

count = 0 

a_dict ={}
b_dict = {}

a_sum = 0 
b_sum = 0 

for i in range(len(A)):
    ssum =0
    for j in range(i, len(A)):
        ssum+=A[j] # a_sum = sum(A[i:j]) - 이렇게 하면 배열 길이 1일 때를 제대로 못 샌다
                    # 슬라이싱 이슈 ... - sum(A[i:j+1])로 해주면 된다 
        if ssum in a_dict:
            a_dict[ssum]+=1
        else :
            a_dict[ssum]=1

for i in range(len(B)):
    ssum = 0 
    for j in range(i, len(B)):
        ssum += B[j] # b_sum = sum(B[i:j]) # 슬라이싱 이슈 ... - sum(B[i:j+1])
        if ssum in b_dict:
            b_dict[ssum]+=1
        else : 
            b_dict[ssum]=1

for A_sum, that_cnt in a_dict.items():
    if T-A_sum in b_dict:
        count += that_cnt*b_dict[T-A_sum]
        
        
print(count)




# T = int(input())
# n = int(input())
# A = list(map(int, input().split()))
# m = int(input())
# B = list(map(int, input().split()))


# # 부분 배열 (연속됨) - Two Pointer 두 개!!!! 
# # Two Pointer의 시간 복잡도 O(n)

# a_left = 0
# a_right = 0
# b_left = 0 
# b_right = 0

# a_sum =0
# b_sum = 0 
# cnt = 0 

# def twopointer(a_left, a_right, b_left, b_right):
#     global cnt 
    
#     if a_left>a_right or b_left>b_right or a_left>=len(A) or b_left>=len(B) or a_right>len(A) or b_right>len(B):
#         return 
    
#     a_sum = sum(A[a_left:a_right])
#     b_sum = sum(B[b_left:b_right])
    
#     if a_sum+b_sum==T : 
#         # if a_left==a_right or b_left==b_right:
#         #     return
#         print(a_sum, b_sum, a_sum+b_sum)
#         cnt +=1
#         return 
#     elif a_sum+b_sum<T : 
#         twopointer(a_left, a_right+1, b_left, b_right)
#         twopointer(a_left, a_right, b_left, b_right+1)
#     else: 
#         twopointer(a_left+1, a_right, b_left, b_right)
#         twopointer(a_left, a_right, b_left+1, b_right)
        
# twopointer(0, 0, 0, 0)
# print(cnt)
