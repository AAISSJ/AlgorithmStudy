


# DP

## 1. 개념 및 기본 풀기 

1. 테이블 정의하기
2. 점화식 찾기
3. 초기값 정하기

<br>

## 2. Top-down & Bottom-up (BOJ 2597 계단오르기) 
### Top-down 
```python
import sys

input = sys.stdin.readline
N = int(input())

stair = [int(input()) for _ in range(N)] + [0]

dp = [[-1] * 3 for _ in range(N)]  # 계단을 1개 밟고 올때와 2개 밟고 올때 나눠서 DP


def dfs(cur, cnt):
    if cnt > 2:
        return -100000000

    if cur > N - 1:
        return -100000000
    elif cur == N - 1:
        return 0

    if cur != -1 and dp[cur][cnt] != -1:
        return dp[cur][cnt]

    ret = max(dfs(cur + 1, cnt + 1) + stair[cur + 1], dfs(cur + 2, 1) + stair[cur + 2])

    dp[cur][cnt] = ret

    return dp[cur][cnt]


print(dfs(-1, 0))
```

<br>

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

<br>


## 3. 2차원 DP 배열 (BOJ 1149 RGB거리)
```python

```



