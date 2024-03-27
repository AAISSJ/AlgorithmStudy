# DP -> 점화식 세우기 
# arr[i,j] = arr[0,j] - arr[0,i-1]
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())
arr = [0]+ list(map(int, input().split()))
sum_arr = [0 for i in range(N+1)]
total = 0


for i in range(1, N+1):
    total += arr[i]
    sum_arr[i]+=total 


for _ in range(M):
    i,j = map(int, input().split())
    print(sum_arr[j]-sum_arr[i-1])
     
