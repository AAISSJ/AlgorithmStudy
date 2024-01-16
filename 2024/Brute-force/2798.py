N, M = map(int, input().split()) # 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000) -> Brute-force로 풀어도 최대 10^6 < 10^8
arr = list(map(int, input().split()))

max_num = 0 

for i in range(0,N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      sum = arr[i]+arr[j]+arr[k] 
      if sum<=M and sum>max_num:
        max_num = sum 

print(max_num)
