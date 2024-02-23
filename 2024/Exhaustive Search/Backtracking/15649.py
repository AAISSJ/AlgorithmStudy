# Backtracking
# - Promising : 해당 루트가 조건에 맞는지 검사 & Pruning : 조간에 맞지 않으면 자른다 
# - dfs (재귀) 기반으로 풀되, Pruning한다는 점이 다름 

N,M = map(int, input().split())
arr = [] 

def backtracking():
    if len(arr)==M :
        print(" ".join(map(str, arr)))
        return 
    
    for i in range(1,N+1):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()
    
backtracking()
