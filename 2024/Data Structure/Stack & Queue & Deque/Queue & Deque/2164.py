from collections import deque
import sys

input = sys.stdin.readline


N = int(input())
dq= deque([i+1 for i in range(0, N)])

while True: 
    if len(dq)==1:
        break
  
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])
