from collections import deque

N,K = map(int, input().split())
dq= deque([i+1 for i in range(0, N)])

string='<'
while True: 
    for i in range(K-1):
        dq.append(dq.popleft())
    string+=str(dq.popleft())
    if len(dq)==0:
        string+='>'
        break
    else :
        string+=', '

print(string)
