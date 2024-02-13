
import sys 
input = sys.stdin.readline


N, S = map(int, input().split())
arr = list(map(int, input().split()))

# arr.sort() -> 왜 sort()하면 안 되는 거지? ... 모르겠다

# 모든 문제는 완전 탐색 먼저 
# min_num = N+1
# flag = 0 
# for i in range(1,len(arr)): # 연속된 수의 길이 
#     for j in range(0,len(arr)-i):
#         if sum(arr[j:j+i])>=S:
#             min_num=i
#             flag = 1
#             break
#     if flag == 1:
#         break 
# print(min_num)

# Two Pointer 로 풀면 된단다
# O(N^2) 걸리는 문제를 O(N) 복잡도로 풀 수 있다
# 단, 배열에 자연수가 아닌 음수가 섞여 있을 때, end를 증가시킨다 해도 부분합이 늘어난다는 보장이 없으므로 
# 이때는 two pointer 사용할 수 없다 
# Q. 그럼 two pointer는 자연수 배열의 부분합 문제에서만 쓸 수 있는 것인가?????
# 2143 두 배열의 합 문제도 비슷하게 풀면 된다 
subtotal=0
left= 0 
right=0
answer= 100001

# 종료 조건 
while True:
    if subtotal<S:
        if right==len(arr):
            break
        subtotal+=arr[right]
        right+=1
    else: 
        subtotal-=arr[left]
        left +=1 
        answer = min(answer, right-left+1)

if answer ==100001:
    print(0)
else:
    print(answer)
