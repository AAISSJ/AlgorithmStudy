def solution(food):
    answer=[]
    # 첫 번째 선수에 대해서 
    for i in range(1, len(food)):
        num = food[i]//2
        for j in range(num):
            answer.append(i)
        if i==len(food)-1:
            answer.append(0) 
    # 거꾸로 넣어줌 
    answer+=list(reversed(answer[:-1]))
    # int list to str     
    answer = ''.join(map(str,answer)) 
    return answer

def solution(food):
    answer=[]
    # 첫 번째 선수에 대해서 
    for i in range(1, len(food)):
        for _ in range(food[i]//2):
            answer.append(i)
    
    # 거꾸로 넣어줌 
    answer=answer+[0]+answer[::-1]
    
    # int list to str     
    answer = ''.join(map(str,answer)) 
    return answer
