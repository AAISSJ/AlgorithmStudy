N = int(input())
 
students = list(map(int, input().split())) 
 
stack = []
 
flag = 1
for student in students:
    stack.append(student)
    while stack and stack[-1] == flag:
        stack.pop() 
        flag +=1 

if stack: 
    print('Sad') 
else:
    print('Nice')
