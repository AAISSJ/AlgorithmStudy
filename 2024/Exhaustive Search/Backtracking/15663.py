import sys 

input = sys.stdin.readline 

N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = [] 
idx_arr = []
dic = {}
def recursion(cnt):
    if cnt==M:
        dic[' '.join(map(str, tmp))] = 0
        return 
    
    for idx, i in enumerate(arr):
        if idx not in idx_arr:
            tmp.append(i)
            idx_arr.append(idx)
            recursion(cnt+1)
            tmp.pop()
            idx_arr.pop()
    
recursion(0)

for string in dic.keys():
    print(string)
