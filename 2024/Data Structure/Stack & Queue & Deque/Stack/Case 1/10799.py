import sys 
input = sys.stdin.readline


string = input()
stack = []

stick = 0
cnt = 0 
string=string.replace('()','_')


for char in string : 
    if char == '(':
        stick += 1 
        stack.append(char)
    elif char == '_':
        cnt+=stick 
    elif char==')':
        stick -=1
        cnt += 1

print(cnt)
        
