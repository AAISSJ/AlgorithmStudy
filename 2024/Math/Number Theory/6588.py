# 파이썬 너무 느리다 ... 시간 초과 몇 번이나 났는데 그냥 맨 처음부터 input = sys.stdin.readline 해줄 걸 ... 
# 그래도 처음 접근 아예 틀린 건 아니고, 소수 배열 while문 돌기 전에 최대로 만들어두는 것!!!!!
import sys 
input = sys.stdin.readline

def make_primes(num): 
    count_dic = {i:True for i in range(0, num+1)}
    count_dic[0]=False
    count_dic[1]=False
    for i in range(2, num+1):
        if count_dic[i]: # True라면
            for j in range(i*i, num+1, i):
                count_dic[j]=False
    return count_dic

# make prime num array 
count_dic= make_primes(1000000)
# 소수배열을 순회하지만, 소수가 아닌 숫자가 더 많아 소수만 따로 담는 배열과 딕셔너리를 이용해 순회시간단축!
new_dic = {}
for i in range(3,1000001):
    if count_dic[i]:
        new_dic[i]=1

while True: 
    N = int(input())
    if N == 0 : 
        break  
    flag = 0 
    for i in new_dic:
        if N-i in new_dic:
            print(f'{str(N)} = {str(i)} + {str(N-i)}')
            flag =1
            break 
    if flag == 0 : 
        print("Goldbach's conjecture is wrong.")
  
# 맨 처음 코드 - 접근은 맞았는데 매번 소수 배열 만들어주는 게 아니라 
# 최초에 딱 한 번만 생성해주는 것이 시간이 덜 든다 
# while True : 
#     n = int(input())
    
#     if n==0:
#         break 
    
#     # count all prime 
    
#     a = [False,False] + [True]*(n-1)
#     primes={}
#     for i in range(2,n+1):
#         if a[i]:
#             primes[i]=1
#             for j in range(2*i, n+1, i):
#                 a[j] = False

#     flag = 0
#     for i in primes:
#         if n-i in primes:
#             if n%2==1 and (n-i)%2==1:
#                 print(f'{str(n)} = {str(i)} + {str(n-i)}')
#                 flag = 1
#                 break 

#     if flag ==0:
#         print("Goldbach's conjecture is wrong.")

    
