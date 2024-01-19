from sys import stdin


def input():
    return stdin.readline().rstrip()


N,M = map(int, input().split()) # input 때문에 시간 초과 남 ;; 

dic_1 = {}
dic_2 = {}
for i in range(N):
  string = input()
  dic_1[string]=i+1
  dic_2[i+1]=string

for j in range(M):
  string = input()
  if string.isdigit():
    print(dic_2[int(string)])
  else :
    print(dic_1[string])
