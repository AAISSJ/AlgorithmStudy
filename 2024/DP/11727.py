import sys

input =sys.stdin.readline

N = int(input())
DP = [0 for i in range(N+1)]


for i in range(1,N+1):
    if i==1:
        DP[i]=1
    elif i==2:
        DP[i]=3
    else:
        DP[i] = DP[i-1]+2*DP[i-2]
    
print(DP[N]%10007)
