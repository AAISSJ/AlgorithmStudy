


# DP

## 1. 개념 및 기본 풀기 

1. 테이블 정의하기
2. 점화식 찾기
3. 초기값 정하기


## 2. Top-down & Bottom-up (BOJ 2597 계단오르기) 
### Top-down 
```python
def dfs(k):
    if dy[k]>0:
        return dy[k]
    if k==1 or k==2:
        return k
    else : 
        dy[k]=dfs(k-1)+dfs(k-2)
        return dy[k]

if __name__=='__main__':
    n=int(input())
    dy=[0]*(n+1)
    print(dfs(n))
```


### Bottom-up
```python
import sys

input = sys.stdin.readline
N = int(input())

stair = [int(input()) for _ in range(N)] + [0]
dp = [0] * (N + 1)
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
for i in range(2, N):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[-2])
```
