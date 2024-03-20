import sys
input = sys.stdin.readline 

N = int(input())
DP = [0 for i in range(N+1)]

for i in range(1,N+1):
    if i==1:
        DP[i] = 0
    elif i ==2 : 
        DP[i]=1 
    elif i==3:
        DP[i]=1
    else : 
        DP[i]=DP[i-1]+1
        if i%2==0:
            DP[i] = min(DP[i], DP[i//2]+1)
        if i%3==0:
            DP[i] = min(DP[i],DP[i//3]+1)

print(DP[N])
