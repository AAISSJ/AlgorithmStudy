import sys 
input = sys.stdin.readline 


N = int(input())

distance=list(map(int,input().split()))
gas = list(map(int,input().split()))

min_num = 10**9+1
answer = 0 
for i in range(len(distance)): 
    if min_num>gas[i]:
        min_num = gas[i]
    answer += min_num*distance[i]

print(answer)
    
