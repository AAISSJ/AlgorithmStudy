M, N = map(int, input().split())
arr = []

for i in range(M):
    arr.append(input())


tmp = []
for i in range(0, M-8+1):
    for j in range(0,N-8+1):
    # 8x8 바둑판 
    # 'B'로 시작 
        cnt = 0 
        for x in range(0,8):
            for y in range(0,8):
                if (x%2==0 and y%2==0) or  (x%2==1 and y%2==1):
                    if not arr[i+x][j+y]=='B':
                        cnt +=1
                else : 
                    if not arr[i+x][j+y]=='W':
                        cnt +=1 
                        
        tmp.append(cnt)
    # 'W'로 시작 
        cnt = 0 
        for x in range(0,8):
            for y in range(0,8):
                if (x%2==0 and y%2==0) or  (x%2==1 and y%2==1):
                    if not arr[i+x][j+y]=='W':
                        cnt +=1
                else : 
                    if not arr[i+x][j+y]=='B':
                        cnt +=1 
                        
        tmp.append(cnt)
print(min(tmp))
