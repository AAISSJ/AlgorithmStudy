import sys
input = sys.stdin.readline 

def backtracking(cnt):
    if cnt==6:
        print(' '.join(map(str, check)))
        return 
    for num in target:
        if num not in check:
            if not check or check[-1]<=num: 
                check.append(num)
                backtracking(cnt+1)
                check.pop()
        

while True : 
    arr = list(map(int,input().split()))
    if arr[0]==0:
        break 
        
    target= arr[1:]
    check= []
    backtracking(0)
    print()
