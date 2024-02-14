

# 인덱스 트리 
# https://programming119.tistory.com/173
# 사용 조건 : 배열 A기 있을 때, 다음의 연산을 여러 번 (M번) 수행해야 하는 경우 
# 1. 구간 l,r이 주어졌을 때, A[l]+ .... + A[r]을 구하여라 
# 2. i번째 수 A[i]를 V로 바꿔라 
# 인덱스 트리를 사용하면 1번 연산, 2번 연산 모두 O(logN)에 수행할 수 있다 -> 여러 번 수행하니 O(MlogN)


# 1. 입력 받기 
N, M, K = map(int,input().split())

arr = []
for _ in range(N):
    array.append(int(input))


M_arr = [] 
K_arr = []


for _ in range(M):
    M_arr.append(list(map(int, input().split())))
    
for _ in range(K):
    K_arr.append(list(map(int, input().split())))
    

# 2. 
