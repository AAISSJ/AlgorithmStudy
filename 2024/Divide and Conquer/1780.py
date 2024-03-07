import sys 

input = sys.stdin.readline 

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

dic = {-1:0,0:0,1:0}
def recursion(start_x,start_y,n):
    target = arr[start_x][start_y]
    flag=0
    for i in range(n):
        for j in range(n):
            if arr[start_x+i][start_y+j]!=target:
                flag =1
                break
    
    if flag==0:
        # print(start_x,start_y,n,target)
        dic[target]+=1
        return 
    else: 
        for i in range(3):
            for j in range(3):
                recursion(start_x+(n//3)*i,start_y+(n//3)*j, n//3)
        return 
    

recursion(0,0,N)

for value in dic.values():
    print(value)
