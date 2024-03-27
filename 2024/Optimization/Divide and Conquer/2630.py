import sys 
input = sys.stdin.readline 

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dic = {0:0,1:0}

# 분할 정복 
# 재귀적으로 푼다 

def recursion(start_x, start_y, length):
    target = graph[start_x][start_y]
    flag = 0 
    for x in range(length):
        for y in range(length):
            if target != graph[x+start_x][y+start_y]:
                flag = 1
                break 
    if flag ==0: 
        dic[target]+=1
        return 
    else: 
        for x in range(2):
            for y in range(2):
                recursion(start_x+(length//2)*x, start_y+(length//2)*y, length//2)
    

recursion(0,0,N)

for i in dic.values():
    print(i)

