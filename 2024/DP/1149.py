import sys 
input = sys.stdin.readline 


N = int(input())
house_arr = [[]]

for _ in range(N):
    house_arr.append(list(map(int,input().split())))

DP = [[0]*3 for i in range(N+1)]    


DP[1][0] = house_arr[1][0]
DP[1][1] = house_arr[1][1]
DP[1][2] = house_arr[1][2]

for i in range(2,N+1):
    DP[i][0] = min(DP[i-1][1],DP[i-1][2]) +house_arr[i][0]
    DP[i][1] = min(DP[i-1][0],DP[i-1][2]) +house_arr[i][1]
    DP[i][2] = min(DP[i-1][0],DP[i-1][1]) +house_arr[i][2]
    
print(min(DP[N]))
