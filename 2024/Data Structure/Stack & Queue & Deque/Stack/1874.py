import sys
input = sys.stdin.readline

n = int(input())

stack = [0,1,]
result = ['+', ]
append_num = 1 
flag = 0

for _ in range(n):
    num = int(input())
    while True:
        if stack[-1]==num:
            stack.pop()
            result.append('-')
            break
        elif stack[-1]<num:
            append_num += 1
            stack.append(append_num)
            result.append('+')
        else:
            flag = 1 
            break 
    if flag == 1:
        break 

if flag == 1:
    print("NO")
else :
    print('\n'.join(result))
