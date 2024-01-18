N, M = map(int, input().split())

set_list = {}
for i in range(N):
  set_list[input()]=0

cnt =0 
for i in range(M):
  check= input()
  if check in set_list:
    cnt+=1

print(cnt)
