import sys
input = sys.stdin.readline 

M,N = map(int, input().split())
# 소수 구하기 -> 에라토스테네스의 체 
arr = [False,False]+[True]*N


def prime(N):
    for i in range(N+1):
        if arr[i]:
            for j in range(i*i, N+1, i):
                arr[j]=False
            if i>=M:
                print(i)
    
prime(N)

    
