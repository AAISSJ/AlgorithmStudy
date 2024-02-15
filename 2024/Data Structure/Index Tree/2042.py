# 인덱스 트리 
# https://programming119.tistory.com/173
# 사용 조건 : 배열 A기 있을 때, 다음의 연산을 여러 번 (M번) 수행해야 하는 경우 
# 1. 구간 l,r이 주어졌을 때, A[l]+ .... + A[r]을 구하여라 
# 2. i번째 수 A[i]를 V로 바꿔라 
# 인덱스 트리를 사용하면 1번 연산, 2번 연산 모두 O(logN)에 수행할 수 있다 -> 여러 번 수행하니 O(MlogN)

# 0. 입력받기
import sys
input = sys.stdin.readline
from math import ceil, log

N, M, K = map(int,input().split())

l = []
segment_tree = [0]*(N*4)


# 1. 트리 만들기
def init(start, end, index):
	# start와 end가 같다면 리프노드이다.
    if start == end:
        segment_tree[index] = l[start-1]
        return segment_tree[index]
	
    # 현재 노드는 왼쪽 아래 노드와 오른쪽 아래 노드를 더한 값이다.
    mid = (start+end) // 2
    segment_tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return segment_tree[index]

       
# 2. 트리에서 값 찾기
def find(start, end, index, left, right):
	# 찾으려는 범위가 start~end 범위보다 클 경우
    if start > right or end < left:
        return 0
        
    # 찾으려는 범위가 segment tree 노드안에 구현되어 있을 경우
    if start >= left and end <= right:
        return segment_tree[index]

	# 코드를 동작시키기 위한 기본 코드
    # 현재 노드는 왼쪽아래 + 오른쪽아래 노드이다.
    mid = (start + end) // 2
    sub_sum = find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right)
    return sub_sum


# 3. 트리 값 바꿔주기
def update(start, end, index, update_idx, update_data):
	# update 하려는 범위가 초과될 경우
    if start > update_idx or end < update_idx:
        return
    
    segment_tree[index] += update_data
	
    # 리프노드까지 바꿔주었으면 재귀함수를 끝낸다.
    if start == end:
        return

	# 내가 관여하고 있는 노드들을 찾아서 바꿔준다 -> 재귀함수로 구현
    mid = (start + end) // 2
    update(start, mid, index*2, update_idx, update_data)
    update(mid+1, end, index*2+1, update_idx, update_data)


for _ in range(N):
    l.append(int(input()))

init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        temp = c - l[b-1]
        l[b-1] = c
        update(1, N, 1, b, temp)

    elif a == 2:
        print(find(1, N, 1, b, c))

### 내가 짠 거 .. 반례 못 찾겠음 
# import sys 
# input = sys.stdin.readline

# # 1. 입력 받기 
# N, M, K = map(int,input().split())

# # 2. 배열 초기화 
# len_arr = 1 
# while True: 
#     if len_arr>N : 
#         break 
#     else : 
#         len_arr*=2

# # 2-1. 리프 노드 채우기         
# arr = [0 for _ in range(len_arr*2)]
# for i in range(N):
#     arr[i+len_arr]=int(input())

# # 2-2. 부모 노드 채우기 -> 구간 합 구하는 문제 ㅇㅇ 
# # for i in range(len(arr)-1, 0,-1):
# #     arr[i//2]+=arr[i]

# for i in range(len_arr-1, 0,-1):
#     arr[i]=arr[i*2]+arr[(i*2)+1]


# def SUM( left, right):
#     left += len_arr-1
#     right += len_arr-1
    
#     result = 0 
#     while(left<=right):
#         if left%2==1:
#             result += arr[left]
#             left+=1
#         if right%2==0:
#             result += arr[right]
#             right-=1
#         left //=2
#         right //=2
    
#     return result
# # L이 right child를 가리키면, result에 값 2을 더하고 l++
# # r이 left child를 가리키면, result에 값 5을 더하고 r--
# # l이 right child를 가리키면 result에 값 7 더하고 l++
# # l,r pointer가 교차되어 loop 종료 

# def UPDATE(index, value):
#     tree_index = len_arr+index-1
    
#     arr[index] =value
#     tree_index//=2
    
#     while tree_index>0:
#         arr[tree_index] = arr[tree_index*2]+arr[(tree_index*2)+1]
#         tree_index//=2
    
# # 3. 연산 시작
# for _ in range(M+K): # 10^5 
#     a, b, c = map(int, input().split())
#     if a == 1:
#         # 3-1. b 번째 숫자 c로 변경 
#         # 숫자 변경 시에 주의해야 할 점은 값을 업데이트하는 것이다 
#         # index = b+len_arr-1
#         # old_num = arr[index]
#         # arr[index]=c
#         # while True: 
#         #     if index == 0 : 
#         #         break 
#         #     arr[index//2]=arr[index//2]-old_num+c
#         #     index = index//2 
#         # print(arr)
#          UPDATE(b, c)
        
#     elif a==2:
#         # 3-2. b~c번째 숫자 간 구간 합 구하기 
#         # 1) 빠지는 인덱스를 구하고 걔만 빼주기  
#         # not_include = [i for i in range(1, N+1) if i<b or c<i]
#         # answer = arr[1]
#         # for i in not_include:
#         #     answer -=arr[len_arr-1+i]
#         print(SUM(b, c))
    
