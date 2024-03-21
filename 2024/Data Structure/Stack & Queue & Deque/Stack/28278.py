import sys

input = sys.stdin.readline

N = int(input())


stack = []

for i in range(N):
    comm = list(map(int, input().split()))

    if comm[0]==1:
        stack.append(comm[1])
    elif comm[0]==2:
        if stack: 
            print(stack.pop())
        else: 
            print(-1)
    elif comm[0]==3:
        print(len(stack))
    elif comm[0]==4:
        if not stack:
            print(1)
        else : 
            print(0)
    else : 
        if stack:
            print(stack[-1])
        else:
            print(-1)
