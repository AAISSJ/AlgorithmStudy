import sys 
input = sys.stdin.readline 

A,B = map(int, input().split())
cnt = 0 

def recursion(num):
    global cnt
    if num==A:
        return cnt
    elif num==0:
        cnt = -1
        return 
    
    if num%10==1:
        num=num//10
        cnt +=1 
        recursion(num)
    elif num%2==0:
        cnt+=1
        recursion(num//2)
    else:
        cnt = -1
        return 
    
    
recursion(B)

if cnt==-1:
    print(-1)
else: 
    print(cnt+1)

# 다른 풀이 1. while문으로 푼 거 
#
# import sys
# input=sys.stdin.readline
# a,b=map(int,input().split())
# count=1
# while True:
#     if b==a:
#         break
#     elif (b%2!=0 and b%10!=1)or (b<a):
#         count=-1
#         break
#     else:
#         if b%10==1:
#             b//=10
#             count+=1
#         else:
#             b//=2
#             count+=1
# print(count)

# 다른 풀이 2. bfs로 푼 사람 
# 
# import sys
# import collections

# input = sys.stdin.readline

# a, b = map(int, input().split())
# queue = collections.deque()

# queue.append(a)


# def bfs():
#     cnt = 1
#     while queue:
#         size = len(queue)
#         for _ in range(size):
#             cur = queue.popleft()
#             if b < cur:
#                 continue
#             if cur == b:
#                 queue.append(a)
#                 print(cnt)
#                 return
#             else:
#                 queue.append(cur * 2)
#                 queue.append(cur * 10 + 1)
#         cnt += 1


# bfs()
# if not queue:
#     print(-1)



    
