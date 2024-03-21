from collections import deque
import sys
input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()
N = int(input().rstrip())

for i in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == "P":
        left.append(cmd[1]) 
    if cmd[0] == "L":
        if left: 
            right.appendleft(left.pop()) 
    if cmd[0] == "D":
        if right:  
            left.append(right.popleft()) 
    if cmd[0] == "B":
        if left: 
            left.pop() 

print("".join(left + right))
