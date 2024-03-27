
N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
num_list = list(map(int, input().split()))



# 풀이 1 - 해시 탐색 : 메모리는 많이 먹지만 더 빠른 듯
dic ={}

for card in card_list:
  dic[card] = 0

for num in num_list : 
  if num in dic:
    print('1',end=' ')
  else: 
    print('0', end=' ')


# 풀이 2 - 이분 탐색 
card_list.sort()

for num in num_list : 
  low, high = 0, N-1
  exit = 0 
  while low<=high:
    mid = (low+high)//2
    if num > card_list[mid] :
      low = mid+1
    elif num < card_list[mid]:
      high=mid-1
    else : 
      exit = 1
      break
  print(exit, end=' ')
