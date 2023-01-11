def solution(answers):
    answer=[]
    score=[]
    give = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 답 개수 세기 
    for i in range(len(give)):
        tmp = give[i]
        cnt = 0 
        for j in range(len(answers)):
            # score.append(tmp[j//len(tmp)])
            if answers[j]==tmp[j%len(tmp)]:
                cnt +=1
        score.append(cnt)
    
    # 순위 정렬하기 
    max_score = max(score)
    for i in range(len(score)):
        if score[i]==max_score:
            answer.append(i+1)
    
    return answer
