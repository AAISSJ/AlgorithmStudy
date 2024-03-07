import sys 

input = sys.stdin.readline 
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0 
right = len(arr)-1
close_num = 10**10+1 
answer = None

while True:
    if right<=left:
        break 
    target = arr[left]+arr[right]
    
    if target<0:
        if abs(target)<close_num:
            close_num = abs(target)
            answer = [arr[left],arr[right]]
        left +=1
    elif target>0:
        if abs(target)<close_num:
            close_num = abs(target)
            answer = [arr[left],arr[right]]
        right-=1
    else : 
        close_num =0 
        answer = [arr[left],arr[right]]
        break 
    
print(' '.join(map(str, answer)))
