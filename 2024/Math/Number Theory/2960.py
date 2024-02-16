n,m = map(int, input().split())


# count all primes - 시간 복잡도 줄이기 위해 해시 사용 
a = {i:True for i in range(2,n+1)} # [False,False] + [True]*(n-1)
a[0], a[1]= False, False
# primes={}

cnt = 0
flag = 0 
answer = 0 
for i in range(2,n+1): # O(Nlog(N))
    if a[i]:
        for j in range(i, n+1, i):
            if a[j]:
                a[j] = False
                cnt+=1
                if cnt==m:
                    flag = 1
                    break
        if flag ==1:
            break

print(j)
