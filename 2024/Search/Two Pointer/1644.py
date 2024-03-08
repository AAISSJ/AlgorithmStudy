import sys 
input = sys.stdin.readline

N= int(input())

# 1. make prime arr 
arr = {i:True for i in range(N+1)}
arr[0] = False 
arr[1] = False

def prime(num):
    tmp = []
    for i in range(2, num+1):
        if arr[i]:
            tmp.append(i)
            for j in range(i*i, num+1, i):
                arr[j]=False
    return tmp 
prime_arr =prime(N)

# 2. 연속된 소수의 합으로 나타내기 
# two pointer ! 
cnt = 0 
start = 0 
end = 0
sum_num = 0

while True: 
    if start>=len(prime_arr) or end>len(prime_arr):
        break 
    if sum_num == N : 
        cnt +=1 
        sum_num-=prime_arr[start]
        start+=1 
    elif sum_num<N : 
        if end ==len(prime_arr):
            break 
        sum_num +=prime_arr[end]
        end +=1
    else: 
        sum_num-=prime_arr[start]
        start+=1 

print(cnt)





