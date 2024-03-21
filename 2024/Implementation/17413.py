import sys 

string = input()
stack = []

flag =0 
for c in string: 
    if c=='<':
        if stack : 
            print(''.join(stack)[::-1],end='')
            stack = []
        stack.append(c)
        flag = 1
    elif c=='>':
        stack.append(c)
        print(''.join(stack),end='')
        stack = []
        flag = 0 
    elif c ==' ':
        if flag == 1:
            stack.append(c)
        else:
            print(''.join(stack)[::-1],end='')
            print(c,end='')
            stack = []
    else:
        stack.append(c)

if stack:
    print(''.join(stack)[::-1],end='')
