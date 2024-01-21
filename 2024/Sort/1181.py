N = int(input())

dic = {}

for i in range(N):
    string = input()
    dic[string] = len(string)

result = sorted(dic.items(), key=lambda x:(x[1], x[0]))

for key,item in result:
    print(key)
