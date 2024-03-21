from collections import deque
import sys 

input = sys.stdin.readline

N = int(input())

dq = deque()

for i in range(N):
    comm = input().split()
    if comm[0]=='push':
        dq.append(comm[1])
    elif comm[0]=='front':
        if dq:
            print(dq[0])
        else: 
            print(-1)
    elif comm[0]=='back':
        if dq:
            print(dq[-1])
        else : 
            print(-1)
    elif comm[0]=='pop':
        if dq: 
            print(dq.popleft())
        else:
            print(-1)
    elif comm[0]=='size':
        print(len(dq))
    elif comm[0]=='empty':
        if dq:
            print(0)
        else:
            print(1)
