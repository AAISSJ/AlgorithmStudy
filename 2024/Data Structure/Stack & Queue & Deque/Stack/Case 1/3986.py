import sys 
from collections import deque 

N = int(input())

cnt = 0 
for _ in range(N):
    string = list(input())
    stack = [] 
    for c in string:
        if not stack : 
            stack.append(c)
        else: 
            if stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
    if not stack:
        cnt+=1
    
    
print(cnt)
    
    
    
