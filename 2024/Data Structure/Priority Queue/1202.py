import  sys
import  heapq

# 우선 순위 큐?!? 
# 언제 사용하느냐 ! -> 정리
    # https://underdog11.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Priority-Queues-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90
# 파이썬에서의 우선 순위 큐 
    # https://sxbxn.tistory.com/33
    # heapq랑 PriorityQueue가 있는데, 그 중에선 heapq 속도가 더 빠르다

input = sys.stdin.readline

N,K  =  map(int,input().split()) 
arr  = []

for  _  in  range(N):
    m,v  =  map(int,input().split()) 
    arr.append([m,v]) 
pack  = []
for  _  in  range(K):
    s  =  int(input()) 
    pack.append(s)

# 보석 무게를 일단 가장 작은 애로, 만약 같은 무게라면 그때는 비싼 가격을 담기 
# 가방 무게도 가장 작은 애부터, 그리고 보석 무게와 대소비교해서 담을 수 있는지 없는지를 판단

arr.sort(key=lambda  x : (x[0],-x[1])) # 보석 무게 오름차순, 보석 가치 내림차순
pack.sort() # 가방 무게 오름차순

result  = [] 
total  =  0
for  idx  in  range(K):
    # 가방의 최대 무게가 보석보다 같거나 더 크다면 담을 수 있음
    while  arr  and  pack[idx] >=  arr[0][0]:
        heapq.heappush(result,-arr[0][1]) # 가장 값어치 있는 애 담기
        heapq.heappop(arr)

    if  result:
        total  -= (heapq.heappop(result))

print(total)
