def solution(s):
    answer = 0
    
    x_cnt = 0
    x_cha = None 
    
    y_cnt = 0
    check = 0
    
    for i,cha in enumerate(s):
        if x_cha == None : 
            x_cha = cha
            x_cnt += 1
            check = 1 
        else : 
            if x_cha != cha : 
                y_cnt +=1
            else :
                x_cnt +=1
            
            if y_cnt == x_cnt : 
                answer +=1
                y_cnt = 0 
                x_cnt = 0
                x_cha = None
                check = 0
            else :
                continue
        
    if check == 1 :
            answer +=1    
    return answer
