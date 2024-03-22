import sys 
input = sys.stdin.readline 

N = int(input())
arr=list(map(int,input().split()))

stack = []
record = [] 

for index, num in enumerate(arr):

    while True: 
        if not stack :
            stack.append((num,index+1))
            record.append(0)
            break 

        if stack[-1][0]<num:
            stack.pop()
        else : 
            record.append(stack[-1][1])
            stack.append((num,index+1))
            break 

print(' '.join(map(str,record)))
