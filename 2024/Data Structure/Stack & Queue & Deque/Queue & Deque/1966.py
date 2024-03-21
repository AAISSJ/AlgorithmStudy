from collections import deque

idx =int(input())

for i in range(idx):
  N, M = map(int, input().split())
  importance = deque(list(map(int, input().split())))
  num_idx = deque([i for i in range(N)])

  cnt = 0
  pop_idx =0 

  while True: 
    max_num = max(importance)
  
    if importance[0]<max_num:
      importance.append(importance.popleft())
      num_idx.append(num_idx.popleft())
  
    elif importance[0]==max_num:
      cnt +=1 
      importance.popleft()
      pop_idx=num_idx.popleft()
      if pop_idx==M:
        print(cnt)
        break 
