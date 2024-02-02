import sys

input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    comm = list(input().split())
    if comm[0]=='push':
        stack.append(comm[1])
    elif comm[0]=='top':
        if stack:
            print(stack[-1])
        else: 
            print(-1)
    elif comm[0]=='size':
        print(len(stack))
    elif comm[0]=='empty':
        if stack:
            print(0)
        else: 
            print(1)
    elif comm[0]=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
