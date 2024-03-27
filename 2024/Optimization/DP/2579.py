import sys 
input = sys.stdin.readline 

N = int(input())
arr = [0] 
dp = [0 for i in range(N+1)]

# 배열 입력 
for _ in range(N):
    arr.append(int(input()))

# arr 0 ~ N 
# dp 0 ~ N

for i in range(1, N+1):
    if i==1:
        dp[i]=arr[i]
    elif i==2:
        dp[i]=arr[i]+arr[i-1]
    elif i==3:
        dp[i]=max(arr[i-1]+arr[i],arr[i-2]+arr[i])
    else: 
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

    
print(dp[N])        
        
