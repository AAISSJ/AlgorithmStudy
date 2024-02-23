import sys
input = sys.stdin.readline 

N, M = map(int, input().split())

total = {}
def backtracking(arr): 
    if len(arr)==M: 
        sorted_arr = sorted(arr)
        string = ' '.join(map(str, sorted_arr))
        if string not in total:
            total[string]=1
        return
    
    for i in range(1,N+1):
        if i not in arr: 
            arr.append(i)
            backtracking(arr)
            arr.pop()

backtracking([])

for s in total.keys():
    print(s)
