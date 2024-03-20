import sys 

input = sys.stdin.readline 


N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int,input().split())))

for k in range(N):
    for a in range(N):
        for b in range(N):
            if arr[a][k] and arr[k][b]:
                arr[a][b]= 1
                
for a in range(N):
    for b in range(N):
        print(arr[a][b],end=' ')
    print()
