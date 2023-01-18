def solution(n, lost, reserve):
    answer = 0
    
    # 0. 체육복 개수 세기 
    clothes=[1]*n
    for i in lost : 
        clothes[i-1]-=1
    for i in reserve :
        clothes[i-1]+=1
    
    
    # 1개 있으면 더하기, 
    # 2개 있으면 앞 뒤 확인하고 앞이 비어있으면 더하고 continue, 아니고 뒤가 비어있다면 더하기, 둘 다 아니면 1만 더하기 
    # 0개 있으면 continue   
    for i in range(len(clothes)) : 
        if clothes[i]==1: 
            answer +=1
        elif clothes[i]==2:
            answer +=1
            if i==0:
                if clothes[i+1]==0:
                    answer +=1
                    continue
            elif i==len(clothes)-1:
                if clothes[i-1]==0:
                    answer +=1
                    continue
            else:
                if clothes[i-1]==0:
                    answer+=1
                    continue
                elif clothes[i+1]==0:
                    answer+=1
                    continue  
        else :
            continue
    
    if answer > n :
        answer=n
    
    return answer
