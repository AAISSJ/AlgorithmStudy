import sys
sys.setrecursionlimit(10000)


input = sys.stdin.readline 

N,M = map(int, input().split())
arr=[]
total = {}
def backtracking(start): 
    if len(arr)==M:
        sorted_arr = sorted(arr)
        string = ' '.join(map(str,sorted_arr))
        if string not in total:
            total[string]=1
        return 
    
    for i in range(start,N+1):
        arr.append(i)
        backtracking(i)
        arr.pop()


backtracking(1)

for s in total.keys():
    print(s)
