import sys 
input = sys.stdin.readline 

A,B = map(int, input().split())
cnt = 0 

def recursion(num):
    global cnt
    if num==A:
        return cnt
    elif num==0:
        cnt = -1
        return 
    
    if num%10==1:
        num=num//10
        cnt +=1 
        recursion(num)
    elif num%2==0:
        cnt+=1
        recursion(num//2)
    else:
        cnt = -1
        return 
    
    
recursion(B)

if cnt==-1:
    print(-1)
else: 
    print(cnt+1)
