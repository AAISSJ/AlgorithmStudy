import sys 

input = sys.stdin.readline 

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []
dic= {}
def recursion(cnt):
    if cnt==M:
        print(' '.join(map(str,tmp)))
        return 
    
    for i in arr:
        if not tmp or tmp[-1]<=i:
            tmp.append(i)
            recursion(cnt+1)
            tmp.pop()
    
recursion(0)


