# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 C개 설치 
# 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000) -> 10^9
import sys
input = sys.stdin.readline 


# 0. 입력 받기 
N, C = map(int, input().split())
arr = [] 

for _ in range(N):
    arr.append(int(input()))
arr.sort()

# 2. 파라메트릭 서치 
# 힌트 : mid = 가장 인접한 두 공유기 사이의 거리
# 조건에 만족하는 값 중 가장 큰 값, 가장 작은 값 찾기 -> parametric search 

low = 1 
high = arr[-1]-arr[0]

while low<=high:
    mid = (low+high)//2
    
    # check	   
    cnt = 1
    set_up = arr[0]
    for i in range(1, len(arr)):
        if arr[i]-set_up >= mid:  # mid(거리) 보다 바로이전에 공유기가 설치된 곳과 현재 설치하려는 곳의 거리가 긴 경우
            set_up = arr[i]       # 이전 공유기가 설치된 장소를 저장한 set_up에 공유기를 설치하고 위치를 갱신하여 저장함
            cnt = cnt + 1           
 
    if cnt>=C:
        low = mid+1
    else: 
        high = mid-1


# 조건에 만족하는 값(가장 인접한 두 공유기 사이의 거리) 중 가장 큰 값을 반환해야 하므로 high 출력
print(high)
