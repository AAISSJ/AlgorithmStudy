import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if arr[a]==a :
        return a 
    else: 
        arr[a]=find(arr[a])
        return arr[a]

def union(a,b):
    a_root = find(a)
    b_root = find(b)
    arr[a_root] = b_root

N, M = map(int, input().split())


arr = [i for i in range(N+1)]
# arr = {}
# for i in range(N+1):
#     arr[i]=i


for _ in range(M):
    cmd, a,b = map(int, input().split())
    if cmd ==0:
        union(a,b)
    elif cmd ==1: 
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
        
