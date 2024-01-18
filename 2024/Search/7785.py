N = int(input())

dic = {}
for n in range(N):
  name, log = map(str, input().split())
  if log=='enter':
    dic[name]=log
  else : 
      del dic[name]

names = sorted(dic, reverse=True)

for string in names:
  print(string)
