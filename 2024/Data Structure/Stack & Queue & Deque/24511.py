from collections import deque 
import sys 

input = sys.stdin.readline

N = int(input())
struct = list(map(int,input().split()))
element = list(map(int, input().split()))
M = int(input()) 
insert = list(map(int, input().split()))

dq = deque()

for st, ele in zip(struct, element): # 10^5
  if st == 0:
    dq.appendleft(ele)

for insert_num in insert: # 10^5
  dq.append(insert_num)
  print(dq.popleft(),end=' ')
