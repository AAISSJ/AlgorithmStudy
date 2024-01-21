import sys 
input = sys.stdin.readline

N = int(input()) # 1 ≤ N ≤ 1,000,000
tmp = list(map(int, input().split()))

sort_tmp = sorted(set(tmp))  # nlogn

dic ={}
for index, num in enumerate(sort_tmp): # n 
  dic[num] = index

for i in tmp: # n 
  print(dic[i], end=' ')

# 시간 복잡도 크게 짠 경우
# N = int(input())
# tmp = list(map(int, input().split()))

# sort_tmp = sorted(set(tmp))  # nlogn

# for i in tmp:  # N^2
#   print(sort_tmp.index(i),end=' ')
