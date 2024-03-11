import sys
from collections import deque 
input = sys.stdin.readline 

N, K = map(int, input().split())
weight = [10**9 for i in range(0,100001)]

def bfs(start):
    cnt = 0 
    queue = deque([start])
    weight[start] = 0 
    
    while queue: 
        now_n = queue.popleft()
        if now_n==K:
            cnt+=1
        for next_n in (now_n+1, now_n-1, now_n*2):
            if 0<=next_n<=10**5:
                if weight[next_n]==10**9 or weight[next_n]>=weight[now_n]+1:
                    weight[next_n]=weight[now_n]+1
                    queue.append(next_n)
                
    return cnt 
cnt = bfs(N)

print(weight[K])
print(cnt)
