N = int(input())

tmp = []
for i in range(0, N//3+1):
  for j in range(0, N//5+1):
    if 3*i + j*5 == N : 
      tmp.append(i+j)

if tmp!=[]:
  print(min(tmp))
else : 
  print(-1)
