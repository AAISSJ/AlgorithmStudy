import sys 

input = sys.stdin.readline 

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))
    
def recursion(start_x, start_y, length):
    target = graph[start_x][start_y]
    flag = 0 
    for dx in range(length):
        for dy in range(length):
            if target != graph[dx+start_x][dy+start_y]:
                flag = 1
                break 
    if flag ==0 :
        print(target,end='')
    else:
        print('(',end='')
        for dx in range(2):
            for dy in range(2):
                recursion(start_x+(length//2)*dx, start_y+(length//2)*dy, length//2)
        print(')',end='')


recursion(0,0,N)
