import sys 
input = sys.stdin.readline

N = int(input())
tmp = []
for i in range(N):
  tmp.append(list(map(int, input().split())))

result = sorted(tmp,key=lambda x : (x[1], x[0]))

for x,y in result:
  print(x,y)
