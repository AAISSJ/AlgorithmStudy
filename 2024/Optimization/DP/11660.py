# dp에 대한 점화식 : dp[i][j]=  dp[i-1][j]+dp[i][j-1]+arr[i][j]-dp[i-1][j-1]
# dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]  
import sys 
input = sys.stdin.readline 


N,M = map(int, input().split())
arr = [[0 for i in range(N+2)]]
dp = [[0 for i in range(N+2)]]
# 1. arr 배열 입력 받기 및 dp 배열 초기화 
for _ in range(N):
    tmp = list(map(int,input().split()))
    arr.append([0]+tmp)
    # dp.append([0]+tmp)
    dp.append([0 for i in range(len(tmp)+1)])

# 2. dp 배열에 점화식 이용하여 값 채우기 
for i in range(1, N+1):
    for j in range(1,N+1):
        dp[i][j]= dp[i-1][j]+dp[i][j-1]+arr[i][j]-dp[i-1][j-1]

# 3. 계산해주기 
for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1] 
    print(answer)

