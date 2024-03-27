import sys 

input = sys.stdin.readline 


n = int(input())

DP = [0 for i in range(n+1)]

for i in range(n+1):
    if i==1:
        DP[i]=1
    elif i==2:
        DP[i]=2
    else:
        DP[i] =DP[i-1]+DP[i-2]
        

print(DP[n]%10007)
