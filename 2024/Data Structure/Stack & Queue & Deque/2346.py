from collections import deque


N = int(input())
flags = deque(list(map(int, input().split())))
nums = deque([i+1 for i in range(N)])


flag = 1 
while True: 
    num = nums.popleft()
    flag = flags.popleft()
    print(num,end=' ')
    if len(nums)==0:
        break
  
    if flag>0: 
        for i in range(flag-1):
            nums.append(nums.popleft())
            flags.append(flags.popleft())
    else: 
        for i in range(-flag):
            nums.appendleft(nums.pop())
            flags.appendleft(flags.pop())
