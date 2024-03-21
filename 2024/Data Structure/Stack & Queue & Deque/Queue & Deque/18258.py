from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque()
for i in range(N):
    comm = input().split()

    if comm[0]=='push':
        queue.append(comm[1])
    elif comm[0]=='pop':
        if queue:
            print(queue.popleft()) 
        else: 
            print(-1)
    elif comm[0]=='size':
        print(len(queue))
    elif comm[0]=='empty':
        if len(queue)==0:
            print(1)
        else: 
            print(0)
    elif comm[0]=='front':
        if queue: 
            print(queue[0])
        else:
            print(-1)
    elif comm[0]=='back':
        if queue: 
            print(queue[-1])
        else:
            print(-1)
