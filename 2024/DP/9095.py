import sys 
input = sys.stdin.readline 


T = int(input())
test_arr = []
for _ in range(T):
    test_arr.append(int(input()))

max_num = max(test_arr)
DP = [0 for i in range(max_num+1)]

for i in range(max_num+1):
    if i==1:
        DP[i]=1
    elif i ==2:
        DP[i]=2
    elif i==3:
        DP[i]=4
    else:
        DP[i]=DP[i-1]+DP[i-2]+DP[i-3]
        
for test_num in test_arr:
    print(DP[test_num])
