N = int(input())


for i in range(0,N):
  list_n = list(map(int,list(str(i))))
  num = sum(list_n)+i
  if num == N: 
    print(i)
    break 

if num != N:
  print(0)

##  다른 사람 풀이 -> 이 사람보다 시간이 더 많이 들었는데 형 변환 때문에 그런가 봄 ㅇㅇㅇ
# def hap(n):
#     s=n
#     #수학적으로 자리수를 이용해서 쪼개는법
#     #356 -> 356//10 -> 35 %10 -> 
#     while n>0:
#         s=s+(n%10) #356->6 #35->5 #3->3
#         n=n//10 #35 3 0 
#     return s
# k=int(input()) #251 
# ans=0
# for i in range(1,k):
#     if hap(i)==k:
#         ans=i
#         break
# if ans==0:
#     print("0")
# else:
#     print(ans)
