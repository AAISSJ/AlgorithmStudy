import sys 
# input = sys.stdin.readline

N = int(input())

tmp = []

for i in range(N):
  age, name = input().split()
  tmp.append((int(age),name,i))

result = sorted(tmp,key = lambda x:(x[0],x[2]))

for age, name, order in result:
  print(age, name)
