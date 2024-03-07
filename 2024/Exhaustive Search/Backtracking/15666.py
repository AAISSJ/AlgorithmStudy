import sys 
input = sys.stdin.readline 


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dic = {}
tmp = []
def recursion(cnt):
    if cnt == M :
        dic[' '.join(map(str,tmp))] = 0
        return 
    
    for i in arr:
        if not tmp or tmp[-1]<=i:
            tmp.append(i)
            recursion(cnt+1)
            tmp.pop()    
        
recursion(0)

for string in dic.keys():
    print(string)
