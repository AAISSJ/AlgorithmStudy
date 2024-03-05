# 같은 정수를 $K$개 이하로 포함한 최장 연속 부분 수열의 길이
# -> 조건을 만족하는 부분 수열 -> Two Pointer ! O(N)

import sys
input = sys.stdin.readline 

N, K = map(int, input().split())
arr = list(map(int,input().split()))


left, right= 0, 1 
dic = {arr[0]:1}
max_length = 0 
ans = 1

while True: 
    if max_length<ans:
        max_length = ans
    
    # 종료 조건 
    if right==N:
        break 
    
    target = arr[right]
    if target in dic: 
        if dic[target]>=K:
            dic[arr[left]]-=1
            left += 1
            ans-=1
            continue
        else:
            dic[target] += 1
            right+=1 
            ans+=1
    else : 
        dic[target] = 1
        right+=1 
        ans+=1

print(max_length)


    
