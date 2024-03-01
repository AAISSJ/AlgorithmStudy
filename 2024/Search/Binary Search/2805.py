import sys 
input = sys.stdin.readline


N,M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

low = 0 
mid = None
high = arr[-1]
subtotal = 0
answer = 0

while high>low:
    mid = (high+low)//2
    new_arr = [i for i in arr if mid<=i]
    subtotal = sum([i for i in arr if mid<=i]) - mid*len(new_arr)
    if subtotal==M:
        answer = mid
        break
    elif subtotal>M:
        low = mid+1 
        answer = mid
    else: 
        high = mid 

print(answer)
    

        
