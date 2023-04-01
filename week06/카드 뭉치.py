def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    check_1_or_2= [0]*len(goal)
    check_1=[]
    check_2=[]
    
    for i,word in enumerate(goal) : 
        if word in cards1: 
            check_1_or_2[i] = 1
            check_1.append(cards1.index(word))
        elif word in cards2: 
            check_1_or_2[i] = 2
            check_2.append(cards2.index(word))
        else : 
            return "No"
    
    # 테스트 케이스 주의! 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다
       
    if check_1!=[]: 
        for i in range(0,len(check_1)):
            if i!=check_1[i]:
                return "No"
    if check_2!=[]:
        for i in range(0,len(check_2)):
            if i!=check_2[i]:
                    return "No"

    return answer
ㅋ
