import sys
input = sys.stdin.readline

n = int(input())
DP = [[0, []] for _ in range(n + 1)]
DP[1][0] = 0
DP[1][1] = [1]

for i in range(2, n + 1):
    DP[i][0] = DP[i-1][0] + 1
    DP[i][1] =  [i] + DP[i-1][1]
    if i % 3 == 0 and DP[i // 3][0] + 1 < DP[i][0]:
        DP[i][0] = DP[i // 3][0] + 1
        DP[i][1] = [i] + DP[i // 3][1]
    if i % 2 == 0 and DP[i // 2][0] + 1 < DP[i][0]:
        DP[i][0] = DP[i // 2][0] + 1
        DP[i][1] =[i] + DP[i // 2][1]

print(DP[n][0])
print(' '.join(map(str,DP[n][1])))
