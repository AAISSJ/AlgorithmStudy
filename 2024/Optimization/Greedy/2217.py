import sys 

input = sys.stdin.readline 

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
    
arr.sort(reverse=True)
num = len(arr)

max_weight = 0 

while arr : 
    weight = arr.pop()
    now_weight = weight*num 
    if max_weight<now_weight:
        max_weight = now_weight
    num-=1

print(max_weight)
